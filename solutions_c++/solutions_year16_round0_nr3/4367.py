#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <math.h>
#include <vector>
#include <string>
#include <set>

using namespace std;

typedef unsigned long long int ulli;

/* Para determinar si un numero es primo) */
bool isPrime (int num)
{
    if (num <=1)
        return false;
    else if (num == 2)         
        return true;
    else if (num % 2 == 0)
        return false;
    else
    {
        bool prime = true;
        int divisor = 3;
        double num_d = static_cast<double>(num);
        int upperLimit = static_cast<int>(sqrt(num_d) +1);
        
        while (divisor <= upperLimit)
        {
            if (num % divisor == 0)
                prime = false;
            divisor +=2;
        }
        return prime;
    }
}

void obtenerBases(ulli num, vector <ulli> *v){
	ulli b2,b3,b4,b5,b6,b7,b8,b9;
	b2=0; b3=0; b4=0; b5=0; b6=0; b7=0; b8=0; b9=0;
	ulli aux = num;
	int pos = 0;
	int ud;
	while (num != 0)
	{
		ud = num % 10;
		if (ud != 0)
		{
			b2 = b2 + ud * pow(2,pos);
			b3 = b3 + ud * pow(3,pos);
			b4 = b4 + ud * pow(4,pos);
			b5 = b5 + ud * pow(5,pos);
			b6 = b6 + ud * pow(6,pos);
			b7 = b7 + ud * pow(7,pos);
			b8 = b8 + ud * pow(8,pos);
			b9 = b9 + ud * pow(9,pos);
		}
		num = num / 10;
		pos = pos + 1;
	}
	v->push_back(b2);
	v->push_back(b3);
	v->push_back(b4);
	v->push_back(b5);	
	v->push_back(b6);
	v->push_back(b7);
	v->push_back(b8);
	v->push_back(b9);
	v->push_back(aux);
}

string DecToBin(ulli number)
{
    string result = "";

    do
    {
        if ( (number % 2) == 0 )
            result += "0";
        else
            result += "1";

        number /= 2;
    } while ( number > 0);

    reverse(result.begin(), result.end());
    return result;
} 

ulli dnt(ulli numero, vector<int> vP)
{
	for (int i=0; i<vP.size(); i++)
	{
		if ((numero % vP.at(i)) == 0)
		{
			return vP.at(i);
		}
	}
	return -1; 
}

bool dntprimo(ulli numero, vector<int> vP)
{
	for (int i=0; i<vP.size(); i++)
	{
		if ((numero % vP.at(i)) == 0)
		{
			return true;
		}
	}
	return false; 
}

bool ningunoPrimo(vector <ulli> *v)
{
	for (int i=0; i< v->size(); i++)
	{
		if (isPrime(v->at(i)))
			return false;
	}
	return true;
}

int main(void) {
    /* number of test cases */
    int t,n,j,h,p;
    cin >> t;
    
    vector <int> vP;
    for (int i=2; i<sqrt(pow(2,32)); i++)
    {
		if (isPrime(i))
			vP.push_back(i);
	}

    for(int i=1; i <= t; i++) { //loops for each case
        //cout << "Case #" << i << ":" << endl;
        
        cin >> n; 
        cin >> j; 
        
		cout << "Case #" << i << ":" << endl;	
		
		ulli num = pow(2,n-1) +1; // numero inicial
		ulli numfinal = pow(2,n); // numero final
		
		std::set<ulli> myset;
		
		h=0;
		while (h<j)
		{
			p = rand() % (numfinal - num) + num;
			while (((p % 2) == 0) || myset.find(p)!=myset.end()) 
			{
				// me aseguro de buscar impares (asi se que terimnan en 1)
				// y que ademas no esten en el conjunto (los P que ya agarre)
				p = rand() % (numfinal - num) + num;
			}
				
			ulli binario = std::stoull (DecToBin(p),nullptr,10);
			vector <ulli> vec;
			obtenerBases(binario,&vec);  
			if (ningunoPrimo(&vec))
			{
				if (dntprimo(vec.at(0),vP) && dntprimo(vec.at(1),vP) && dntprimo(vec.at(2),vP) && 
				dntprimo(vec.at(3),vP) && dntprimo(vec.at(4),vP) && dntprimo(vec.at(5),vP) && 
				dntprimo(vec.at(6),vP) && dntprimo(vec.at(7),vP) && dntprimo(vec.at(8),vP))
				{
					cout << binario << " ";
					cout << dnt(vec.at(0),vP) << " "; // base 2
					cout << dnt(vec.at(1),vP) << " "; // base 3
					cout << dnt(vec.at(2),vP) << " "; // base 4
					cout << dnt(vec.at(3),vP) << " "; // base 5
					cout << dnt(vec.at(4),vP) << " "; // base 6
					cout << dnt(vec.at(5),vP) << " "; // base 7
					cout << dnt(vec.at(6),vP) << " "; // base 8
					cout << dnt(vec.at(7),vP) << " "; // base 9
					cout << dnt(vec.at(8),vP) << endl; // base 10
					h=h+1;
					myset.insert(binario);
				}
			}    
			
		}

        
    }

    return 0;

}

