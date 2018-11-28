#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;
int main()
{
    ifstream min ("Wlarge.in");
    ofstream mout ("Warlarge.txt");
    int t;
    min>>t;
    for(int i=0;i<t;i++)
    {
            int n;
            min>>n;
            double a1[1000],a2[1000];
            
            for(int j=0;j<n;j++)
            min>>a1[j];
            
            for(int j=0;j<n;j++)
            min>>a2[j];
            
            
            /*for(int j=0;j<n-1;j++)
            {
                    for(int k=0;k<n-1;k++)
                    {
                            if(a1[k]>a1[k+1])
                            {
                                             double temp = a1[k];
                                             a1[k]=a1[k+1];
                                             a1[k+1]=temp;
                                             }
                            if(a2[k]>a2[k+1])
                            {
                                             double temp = a2[k];
                                             a2[k]=a2[k+1];
                                             a2[k+1]=temp;
                                             }
                            }
                    }
            */
            
            sort(a1,a1+n);
            sort(a2,a2+n);
            
            //for(int j=0;j<n;j++)
            //cout<<a1[j]<<" "<<a2[j]<<endl;
            //cout<<endl<<endl<<endl;
            
            int a1l=0,a1h=n-1,a2l=0,a2h=n-1,dtotal=n;
            
            while(a1[a1h]<a2[a2h]&&dtotal>0)
            {
                                  a2h--;
                                  a1l++;
                                  dtotal--;
                                  }
            
            while(a1[a1l]<a2[a2l]&&dtotal>0)
            {
                                  a2h--;
                                  a1l++;
                                  dtotal--;
                                  
                                  }
    
            for(int j=a1l;j<=a1h;j++)
            {
                    if(a1[a1l]<a2[a2l])
                    {
                                       a1l++;
                                       dtotal--;
                                       }
                    else
                    {
                    a1l++;
                    a2l++;
                    }
                    }
            
            a1l=0;
            a2l=0;
            int total=0;
            for(int j=0;j<n;j++)
            {
                  if(a1[a1l]>a2[a2l])
                  {
                                     a2l++;
                                     total++;
                                     }  
                  else
                  {
                      a1l++;
                      a2l++;
                  }
                    }
                                  
                mout<<"Case #"<<i+1<<": "<<dtotal<<" "<<total<<endl;                  
    
            }
         system("pause");   
    return 0;
}
