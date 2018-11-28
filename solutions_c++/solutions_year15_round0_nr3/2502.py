#include <stdio.h>

const int signTable[4][4] = {
    {1,1,1,1},
    {1,-1,1,-1},
    {1,-1,-1,1},
    {1,1,-1,-1}
};

const int symbolTable[4][4] = {
    {0, 1, 2, 3},
    {1, 0, 3, 2},
    {2, 3, 0, 1},
    {3, 2, 1, 0}
};

int invSymbolTable[4][4];
int invSignTable[4][4];

const char symbolList[] = {'1', 'i', 'j', 'k'};
int invSymbolList[256];

int inputSymbol[10000];
int prefixInputSymbol[20000];
int prefixInputSign[20000];
int suffixInputSymbol[20000];
int suffixInputSign[20000];

void multiply(int sign1, int symbol1, int sign2, int symbol2, int& resSign, int& resSymbol)
{
	resSign = sign1*sign2*signTable[symbol1][symbol2];
	resSymbol = symbolTable[symbol1][symbol2];
}

void power(int sign, int symbol, int power_val, int& resSign, int& resSymbol)
{
	int power_mod = power_val%4;
	resSymbol = invSymbolList['1'];
	resSign = 1;
	for(int i = 0; i < power_mod; i++)
		multiply(resSign, resSymbol, sign, symbol, resSign, resSymbol);
	/*int power_mod = power_val%2;
	int power_div = power_val/2;
	if(symbol == invSymbolList['1'])
	{
	    resSymbol = symbol;
	    if(power_mod == 0)
		resSign = 1;
	    else resSign = sign;    
	}
	else
	{
		if(power_mod == 0)
		{
			resSymbol = invSymbolList['1'];
			resSign = -1;
		}
		else
		{
			resSymbol = symbol;
			resSign = sign;
		}
		if(power_div % 2 != 0)
			resSign = -resSign;
	}*/
}

bool findIJK(long l, long x, int *val, int *prefixSymbolTable, int *prefixSignTable, int *suffixSymbolTable, int *suffixSignTable)
{
    int currentSymbol = invSymbolList['1'], currentSign = 1;//symbol '1', sign +
    int sequenceSymbol, sequenceSign;
    for(int j = 0; j < 2; j++)
    {
	for(int i = 0; i < l; i++)
	{
	    int nextSymbol = symbolTable[currentSymbol][val[i]];
	    int nextSign = signTable[currentSymbol][val[i]] * currentSign;
	    prefixSymbolTable[i+j*l] = nextSymbol;
	    prefixSignTable[i+j*l] = nextSign;
	    currentSymbol = nextSymbol;
	    currentSign = nextSign;
	}
	if(j == 0)
	{
	    sequenceSymbol = currentSymbol;
	    sequenceSign = currentSign;
	}
    }
    for(int i = 0; i < l; i++)
    {
    	int prefixSymbol = i<l-1?prefixSymbolTable[l-i-2]:invSymbolList['1'];
    	int prefixSign = i<l-1?prefixSignTable[l-i-2]:1;
    	suffixSymbolTable[i] = invSymbolTable[sequenceSymbol][prefixSymbol];
    	suffixSignTable[i] = invSignTable[sequenceSymbol][prefixSymbol]*prefixSign*sequenceSign;
    }
    for(int i = 0; i < l; i++)
	multiply(suffixSignTable[i], suffixSymbolTable[i], sequenceSign, sequenceSymbol, suffixSignTable[i+l], suffixSymbolTable[i+l]);
    
    /*for(int i = 0; i < 2*l; i++)
	printf("%c%c ", prefixSignTable[i]==1?' ':'-', symbolList[prefixSymbolTable[i]]);
    printf("\n");
    for(int i = 0; i < 2*l; i++)
	printf("%c%c ", suffixSignTable[i]==1?' ':'-', symbolList[suffixSymbolTable[i]]);
    printf("\n");*/
    
    int fullSymbol, fullSign;
    power(sequenceSign, sequenceSymbol, x, fullSign, fullSymbol);
    if(fullSymbol != invSymbolList['1'] || fullSign != -1)
    	return false;
    int minPosI = -1, minPosK = -1;
    for(int i = 0; i < 2*l; i++)
    {
	if(prefixSymbolTable[i] == invSymbolList['i'])
	{
		if(prefixSignTable[i] == 1)
		{
			minPosI = i;
			break;
		}
		else if(sequenceSymbol != invSymbolList['1'])
			minPosI = i+2*l;//product of the same symbol == -1 (except for 1)
	}
    }
    for(int i = 0; i < 2*l; i++)
    {
	if(suffixSymbolTable[i] == invSymbolList['k'])
	{
		if(suffixSignTable[i] == 1)
		{
			minPosK = i;
			break;
		}
		else if(sequenceSymbol != invSymbolList['1'])
			minPosK = i+2*l;//product of the same symbol == -1 (except for 1)
	}
    }
    //printf("posI : %d posK : %d\n", minPosI, minPosK);
    return minPosI >= 0 && minPosK >= 0 && minPosI+minPosK <= l*x-2;
}

int main()
{
    for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; j++)
        {
            invSymbolTable[symbolTable[i][j]][i] = j;
            invSignTable[symbolTable[i][j]][i] = signTable[i][j];
        }
    for(int i = 0; i < 256; i++)
	invSymbolList[i] = -1;
    for(int i = 0; i < 4; i++)
	invSymbolList[symbolList[i]] = i;
    /*for(int i = 0; i < 4; i++)
    {
        for(int j = 0; j < 4; j++)
        {
            printf("%c%c\t", signTable[i][j]>0?' ':'-', symbolList[symbolTable[i][j]]);
        }
        printf("\n");
    }
    printf("\n");
    for(int i = 0; i < 4; i++)
    {
        for(int j = 0; j < 4; j++)
        {
            printf("%c%c\t", invSignTable[i][j]>0?' ':'-', symbolList[invSymbolTable[i][j]]);
        }
        printf("\n");
    }*/
    int num = 0;
    scanf("%d\n", &num);
    for(int i = 0; i < num; i++)
    {
	long l;
	long x;
	scanf("%ld %ld\n", &l, &x);
	for(int j = 0; j < l; j++)
	{
		char c;
		scanf("%c", &c);
		inputSymbol[j] = invSymbolList[c];
	}
    	printf("Case #%d: %s\n", i+1, findIJK(l, x, inputSymbol, prefixInputSymbol, prefixInputSign, suffixInputSymbol, suffixInputSign)?"YES":"NO");
    }
    return 0;
}
