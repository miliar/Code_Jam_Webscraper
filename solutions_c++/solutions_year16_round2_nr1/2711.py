#include<cstdio>
#include<vector>
using namespace std;
int count[128];
char str[2005];
int num[10];
int main(void)
{
    int T;
    //vector <int> v;
    scanf("%d",&T);
    gets(str);
    for(int i=1;i<=T;i++)
    {
	//v.clear();
        gets(str);
	for(int j=0;j<128;j++)
            count[j]=0;
	for(int j=0;j<10;j++)
            num[j]=0;
        for(int j=0;str[j];j++)
            count[str[j]]++;
        for(;count['Z']>0;count['Z']--)
        {
	    num[0]++;
	    //count['Z'-'A']--;
	    count['E']--;
	    count['R']--;
	    count['O']--;
	}
	for(;count['X']>0;count['X']--)
	{
	    num[6]++;
            count['S']--;
	    count['I']--;
        }
	for(;count['G']>0;count['G']--)
	{
	    num[8]++;
	    count['E']--;
	    count['I']--;
	    count['H']--;
	    count['T']--;
	}
	for(;count['U']>0;count['U']--)
	{
	    num[4]++;
	    count['F']--;
	    count['O']--;
	    count['R']--;
	}
	for(;count['S']>0;count['S']--)
	{
	    num[7]++;
	    count['E']-=2;
	    count['V']--;
	    count['N']--;
	}
	for(;count['F']>0;count['F']--)
	{
            num[5]++;
	    count['I']--;
	    count['V']--;
	    count['E']--;
	}
	for(;count['H']>0;count['H']--)
	{
	    num[3]++;
	    count['T']--;
	    count['R']--;
	    count['E']-=2;
	}
	for(;count['T']>0;count['T']--)
	{
	    num[2]++;
	    count['W']--;
	    count['O']--;
	}
	for(;count['I']>0;count['I']--)
	{
	    num[9]++;
	    count['N']-=2;
	    count['E']--;
	}
	for(;count['O']>0;count['O']--)
	{
	    num[1]++;
	    count['N']--;
	    count['E']--;
	}
	printf("Case #%d: ",i);
	for(int j=0;j<=9;j++)
	    for(int k=0;k<num[j];k++)
		printf("%d",j);
	printf("\n");
    }
    return 0;
}
