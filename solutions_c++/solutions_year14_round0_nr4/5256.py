#include<iostream>
#include<algorithm>
using namespace std;
int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}
int main(){
    freopen ("googlecodejamfirstoutput.txt","w",stdout);
    int t,z;
    cin>>t;
    for(z=1;z<=t;z++)
    {
                    int n;
                    cin>>n;
                    int arrn[n],arrk[n];
                    int i;
                    double d;
                    for(i=0;i<n;i++)
                    {
                                    cin>>d;
                                    arrn[i]=(int)(d*1000000);
                    }
                    for(i=0;i<n;i++)
                    {
                                    cin>>d;
                                    arrk[i]=(int)(d*1000000);
                    }
                    int f=0,countf=0,countnf=0;
                    qsort(arrk,n,sizeof(int),compare);
                    qsort(arrn,n,sizeof(int),compare);
                    //cout<<"rochesky";
                    for(i=0;i<n;i++)
                    {
                           while(arrk[f]<arrn[i]&&f!=n)
                           f++;
                           
                           if(f==n)
                           break;
                           countf++;
                           f++;
                           //cout<<"f"<<f<<"i"<<i<<"n"<<n<<"cout"<<countf;
                    }
                    //cout<<endl<<"overher"<<countf<<endl;
                    countf=n-countf;
                    //cout<<countf<<endl;
                    f=n-1;
                    //cout<<"OK !"<<countf;
                    while(n--)
                    {
                              while(arrk[f]>arrn[n]&&f!=-1)
                              f--;
                              if(f==-1)
                              break;
                              countnf++;
                              f--;
                    }
                    cout<<"Case #"<<z<<": "<<countnf<<" "<<countf<<endl;
    }
    cin.get();
    cin.get();
    
    
    
    }
