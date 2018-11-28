#include<iostream>
#include<fstream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
bool arr[10];
char str[50];
int main()
{
    ifstream f1;
    ofstream f2;
    f1.open("A-large.in");
    f2.open("output.out");
    int c=1,t,x,r,col;
    f1>>t;
    while(c<=t)
    {
    			for(int i=0;i<10;i++)arr[i] = 0;
               f2<<"Case #"<<c++<<": ";
               f1>>x;
               long long int temp = x;
               if(x==0)f2<<"INSOMNIA\n";
               else 
               {
                    col = 0;
                    r = 0;
                    while(col < 10)
                    {
                    	sprintf(str,"%d",x);
                    	//cout<<"\n converted x : "<<str<<" , with len = "<<strlen(str)<<endl;
                    	for(int i=0;i<strlen(str);i++)
						{
							if(!arr[str[i]-'0'])
							{
								arr[str[i]-'0'] = 1 ;
								 col++;	
							}	
						}
                    	x = x + temp;
                    	//r++;
                    //	temp++;
                    }
                    f2<<str<<endl;
			   }
			   
    }
    f1.close();
    f2.close();
    //system("pause");
    return 0;
    }
