#include<fstream>
#include<iostream>
using namespace std;
int ans1(float ken[], float naomi[], int n)
{
    
    int naomi_ans=0;
    for(int j=0;j<n;j++)
            {
                    int def = 0;
                    for(int k=0;k<n;k++)
                            if(naomi[k]>ken[j])
                            {
                                               def=1;
                                               break;
                            }
                    if(def==1)
                    {
                              for(int k=n-1;k>=0;k--)
                              {
                                      if(naomi[k]>ken[j])
                                      {
                                                         naomi[k]=0;
                                                         ken[j]=0;
                                                         naomi_ans++;
                                                         break;
                                      }
                              }
                    }
                    else
                              for(int k=n-1;k>=0;k--)
                                      if(naomi[k]!=0)
                                      {
                                                     naomi[k]=0;
                                                     ken[j]=0;
                                                     break;
                                      }
                    //for(int j=0;j<n;j++)
//                            cout<<naomi[j]<<" ";
//                    cout<<endl;
//                    for(int j=0;j<n;j++)
//                            cout<<ken[j]<<" ";
//                    cout<<endl;
            }
            return naomi_ans;
}
int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("D-large.in");
    fout.open("D-large.out");
    int t, n, ken_ans, naomi_ans;
    float ken[1000], naomi[1000], ken2[1000], naomi2[1000];
    fin>>t;
    for(int i=1;i<=t;i++)
    {
            ken_ans=0;
            naomi_ans=0;
            fin>>n;
            for(int j=0;j<n;j++)
                    fin>>naomi[j];
            for(int j=0;j<n;j++)
                    fin>>ken[j];
            for(int j=0;j<n;j++)
                    for(int k=j+1;k<n;k++)
                    {
                            if(ken[k]>ken[j])
                            {
                                             ken[k]+=ken[j];
                                             ken[j]=ken[k]-ken[j];
                                             ken[k]-=ken[j];
                            }
                    }
            for(int j=0;j<n;j++)
                    for(int k=j+1;k<n;k++)
                    {
                            if(naomi[k]>naomi[j])
                            {
                                             naomi[k]+=naomi[j];
                                             naomi[j]=naomi[k]-naomi[j];
                                             naomi[k]-=naomi[j];
                            }
                    }
            for(int j=0;j<n;j++)
                    naomi2[j]=naomi[j];
            for(int j=0;j<n;j++)
                    ken2[j]=ken[j];
            //for(int j=0;j<n;j++)
//                    fout<<naomi[j]<<" ";
//            fout<<endl;
//            for(int j=0;j<n;j++)
//                    fout<<ken[j]<<" ";
//            fout<<endl;
            naomi_ans = ans1(ken, naomi, n);
            ken_ans = ans1(naomi2, ken2, n);
            fout<<"Case #"<<i<<": "<<naomi_ans<<" "<<n-ken_ans<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
