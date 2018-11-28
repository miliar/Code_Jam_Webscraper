#include<iostream>
#include<fstream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<string>
using namespace std;
int main()
{
    ifstream f1;
    ofstream f2;
    f1.open("A-small-attempt0.in");
    f2.open("output.out");
    int c=1,t,E,R,T,O,H,F,I,V,S,N;
    string str,ans;
    f1>>t;
    while(c<=t)
    {
    	E = R = T = O = H = F = I = V = S = N = 0;
    	f2<<"Case #"<<c++<<": ";
    	f1>>str;
    	ans = "";
    	int len = str.length();
    	//cout<<"str : "<<str<<" , len = "<<len<<endl;
    	for(int i=0;i<len;i++)
    	{
    		if(str[i]=='Z')
			{
				ans += '0';
				E--;R--;O--;
			}
    		if(str[i]=='W')
			{
				ans += '2';
				T--;O--;
			}
    		if(str[i]=='G')
    		{
    			ans += '8';
    			E--;I--;H--;T--;
    		}
    		if(str[i]=='X')
    		{
    			ans += '6';
    			S--;I--;
    		}
    		if(str[i]=='U')
    		{
    			ans += '4';
    			F--;O--;R--;
    		}
    		if(str[i]=='E')E++;
    		if(str[i]=='R')R++;
    		if(str[i]=='T')T++;
    		if(str[i]=='O')O++;
    		if(str[i]=='H')H++;
    		if(str[i]=='I')I++;
    		if(str[i]=='V')V++;
    		if(str[i]=='S')S++;
    		if(str[i]=='F')F++;
    		if(str[i]=='N')N++;
     	}
     	while(true)
     	{
     		if(E==0 && R==0 && O==0 && N==0 && T==0 && H==0 && F==0 && I==0 && V==0 && S==0)break;
     		if(O>0 && N>0 && E>0)
     		{
     			ans += '1';
     			O--;N--;E--;
     		}
     		if(T>0 && H>0 && R>0 && E>1)
     		{
     			ans += '3';
     			T--;H--;R--;E-=2;
     		}
     		if(F>0 && I>0 && V>0 && E>0)
     		{
     			ans += '5';
     			F--;I--;V--;E--;
     		}
     		if(S>0 && E>1 && V>0 && N>0)
     		{
     			ans += '7';
     			S--;E-=2;V--;N--;
     		}
     		if(N>1 && I>0 && N>0 && E>0)
     		{
     			ans += '9';
     			N-=2;I--;E--;
     		}
     	}
     	sort(ans.begin(),ans.end());
     	f2<<ans<<endl;
     	ans = "";
    }
    f1.close();
    f2.close();
    return 0;
    }
