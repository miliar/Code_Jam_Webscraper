#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int main(){
    freopen ("googlecodejamfirstoutput.txt","w",stdout);
    int t,z;
    cin>>t;
    for(z=1;z<=t;z++)
    {
                     cout.precision(7);
                     int i,j;
                     long double a,b,r,c,total,grandtotal,f,x;
                     cin>>c>>f>>x;
                     grandtotal=x/2;
                     total=0;
                     for(i=1;i<3000;i++,total=0)
                     {
                                    r=2;
                                    for(j=1;j<=i;j++)
                                    {
                                        total+=(c/r);
                                        r+=f; 
                                        //cout<<"hi"<<r<<" "<<total<<j<<" "<<i<<endl;            
                                    }
                                    //cout<<total<<endl;
                                    if(grandtotal<(total+x/r))
                                    {
                                                              cout<<std::fixed;
                                                              cout<<"Case #"<<z<<": "<<(long double)grandtotal<<endl;
                                                              //printf("Case #%d: %.7lf\n",z,grandtotal);
                                                              break;
                                    }
                                    else
                                    grandtotal=total+x/r;
                     }
                     
    }
    cin.get();
    cin.get();
    }
