#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
        int tc,i,j,k;
        int n;
        cin>>tc;
        for(i=0;i<tc;i++)
        {
                cin>>n;
                double naomi[n],ken[n];
                int kflag[n],nflag[n];
                for(j=0;j<n;j++)
                {
                    cin>>naomi[j];
                    nflag[j]=0;
                }
                for(j=0;j<n;j++)
                {
                    cin>>ken[j];
                    kflag[j]=0;
                }
                sort(naomi,naomi+n);
                sort(ken,ken+n);
                int index=0;
                int nwin=0,kwin=0;
                for(j=0;j<n;j++)
                {
                    for(k=index;k<n;k++)
                    {
                            if(ken[k]>naomi[j] && kflag[k]==0)
                            {
                                kflag[k]=1;
                                index=k+1;
                                kwin++;
                                break;
                            }
                    }
                    if(k==n)
                        break;
                }
                nwin=n-kwin;    //no.of naomi wins without cheating
               //war completed//

                int ftken=0,endken=n; //first and end indexes of ken
                int ndwin=0;        //no.of naomi wins with cheating
                for(j=0;j<n;j++)
                {
                        for(k=ftken;k<endken;k++)
                        {
                                if(naomi[j]<ken[k])
                                {
                                    endken--;
                                    break;
                                }
                                else if(naomi[j]>ken[k] )
                                {
                                        ndwin++;
                                        ftken++;
                                        break;
                                }
                        }
                }
                //dwar completed
                cout<<"Case #"<<i+1<<": "<<ndwin<< "  "<<nwin<<"\n";
        }
        return 0;
}

