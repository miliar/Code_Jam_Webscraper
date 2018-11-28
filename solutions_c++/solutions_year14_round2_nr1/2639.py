#include<iostream>
#include<string>
#include<cmath>
#include<cstdio>
using namespace std;
int main()
{
    //    freopen("in1.txt","r",stdin);
     //   freopen("out1.txt","w",stdout);
        int tc,n,con;
        cin>>tc;
        int i,j,k;
        string st1,st2;
        string test1,test2;
        for(i=0;i<tc;i++)
        {
                cin>>n;
                cin>>st1>>st2;
                int ct1[100]={0,};
                int ct2[100]={0,};
                test1="";test2="";
                for(j=0;j<st1.length();j++)
                {
                        if(j==0)
                        {
                            test1+=st1[j];
                            ct1[0]++;
                            con=0;
                        }
                        else
                        {
                                if(test1[0]!=st1[j])
                                {
                                    test1=st1[j]+test1;
                                    con++;
                                    ct1[con]++;
                                }
                                else
                                {
                                    ct1[con]++;
                                }
                        }
                }
                //string 2
                for(j=0;j<st2.length();j++)
                {
                        if(j==0)
                        {
                            test2+=st2[j];
                            ct2[0]++;
                            con=0;
                        }
                        else
                        {
                                if(test2[0]!=st2[j])
                                {
                                    test2=st2[j]+test2;
                                    con++;
                                    ct2[con]++;
                                }
                                else
                                {
                                    ct2[con]++;
                                }
                        }
                }
                //compare
                int sum=0;
                if(test1!=test2)
                    cout<<"Case #"<<i+1<<": Fegla Won\n";
                else
                {
                        for(j=0;j<100;j++)
                        {
                                sum+=fabs(ct1[j]-ct2[j]);
                        }
                        cout<<"Case #"<<i+1<<": "<<sum<<"\n";
                }

        }
        return 0;
}
