#include<cstdio>
#include<algorithm>

using namespace std;

int main()
{
int i,j,k,t,T;
char a[2005];
int b[27],c[10];

scanf("%d",&T);

for(t=1;t<=T;t++)
	{
	for(i=0;i<27;i++) b[i]=0;
	for(i=0;i<10;i++) c[i]=0;

	scanf("%s",a);
	for(k=0;a[k];k++) b[a[k]-'A']++;
	
//	printf("O%d \n",b['O'-'A']);
//	printf("Z%d \n",b['Z'-'A']);

	/// ZERO
	c[0]= b['Z'-'A'];
	b['E'-'A']-= b['Z'-'A']; 
	b['R'-'A']-= b['Z'-'A']; 
	b['O'-'A']-= b['Z'-'A']; 
	b['Z'-'A']=0;

//	printf("%d \n",b['O'-'A']);
	/// TWO
	c[2]= b['W'-'A'];
	b['T'-'A']-= b['W'-'A']; 
	b['O'-'A']-= b['W'-'A']; 
	b['W'-'A'] = 0;

//	printf("%d \n",b['O'-'A']);
	// "SIX"
	c[6]= b['X'-'A'];
	b['S'-'A']-= b['X'-'A']; 
	b['I'-'A']-= b['X'-'A']; 
	b['X'-'A'] = 0;

	// "EIGHT"
	c[8]= b['G'-'A'];
	b['E'-'A']-= b['G'-'A']; 
	b['I'-'A']-= b['G'-'A']; 
	b['H'-'A']-= b['G'-'A']; 
	b['T'-'A']-= b['G'-'A']; 
	b['G'-'A'] = 0;
	
	// "THREE"
	c[3]= b['H'-'A'];
	b['T'-'A']-= b['H'-'A']; 
	b['R'-'A']-= b['H'-'A']; 
	b['E'-'A']-= 2*b['H'-'A']; 
	b['H'-'A'] = 0;

	//  "FOUR"
	c[4]= b['R'-'A'];
	b['F'-'A']-= b['R'-'A']; 
	b['O'-'A']-= b['R'-'A']; 
	b['U'-'A']-= b['R'-'A']; 
	b['R'-'A'] = 0;
	
	// "FIVE"
	c[5]= b['F'-'A'];
	b['I'-'A']-= b['F'-'A']; 
	b['V'-'A']-= b['F'-'A']; 
	b['E'-'A']-= b['F'-'A']; 
	b['F'-'A'] = 0;

	// "ONE",
	c[1]= b['O'-'A'];
	b['N'-'A']-= b['O'-'A']; 
	b['E'-'A']-= b['O'-'A']; 
	b['O'-'A'] = 0;

	// "SEVEN",
	c[7]= b['V'-'A'];
	b['S'-'A']-= b['V'-'A']; 
	b['N'-'A']-= b['V'-'A']; 
	b['E'-'A']-= 2*b['V'-'A']; 
	b['V'-'A'] = 0;

	// c"NINE"
	c[9] = b['I'-'A'];


	printf("Case #%d: ",t);
	for(i=0;i<10;i++)
		for(j=0;j<c[i];j++)
			printf("%d",i);
	printf("\n");
	}

return 0;
}
