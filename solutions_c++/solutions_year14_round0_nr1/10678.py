#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ifstream fin("A-small-attempt6.in");
    ofstream fout("output.out");
    int a[4][4],i,j;
    int b[4][4];
    int t;
    int count=0;
	int ans;
    int s1,s2,pingu=0;
    fin.seekg(0);
    fin>>t;
    //cout<<"t: "<<t<<endl;
    
    while(t!=1){
                count++;
             --t;
			 ans=-3;
             s1=s2=pingu=0;
             fin>>s1;
             s1--;
             for (i=0;i<4;i++)
             {
               for (j=0;j<4;j++)
               {
                   fin>>a[i][j];
               }  
             }
             fin>>s2;
             s2--;
             for (i=0;i<4;i++)
             {
               for (j=0;j<4;j++)
               {
                   fin>>b[i][j];
               }  
             }
             
             for (i=0;i<4;i++)
             {
                 for (j=0;j<4;j++)
                 {
                     
                     if (a[s1][i]==b[s2][j])
                     {
                        pingu++;
                        if (pingu>1)
                        {
                           ans=-2;
                        }
                        else
                        {
                            ans = a[s1][i];
                        }
                     }
                 }
                 
             }
			 //cout<<"ans: "<<ans;
			 switch(ans)
             {
               case -2:fout<<"Case #"<<count<<": Bad magician!"<<"\n";
                    break;
               case -3:fout<<"Case #"<<count<<": Volunteer cheated!"<<"\n";
                    break;
               default:fout<<"Case #"<<count<<": "<<ans<<"\n";
                       break;
               
               }

    }
    count++;
    
    ans=-3;
             s1=s2=pingu=0;
             fin>>s1;
             s1--;
             for (i=0;i<4;i++)
             {
               for (j=0;j<4;j++)
               {
                   fin>>a[i][j];
               }  
             }
             fin>>s2;
             s2--;
             for (i=0;i<4;i++)
             {
               for (j=0;j<4;j++)
               {
                   fin>>b[i][j];
               }  
             }
             
             for (i=0;i<4;i++)
             {
                 for (j=0;j<4;j++)
                 {
                     
                     if (a[s1][i]==b[s2][j])
                     {
                        pingu++;
                        if (pingu>1)
                        {
                           ans=-2;
                        }
                        else
                        {
                            ans = a[s1][i];
                        }
                     }
                 }
                 
             }
			 //cout<<"ans: "<<ans;
			 switch(ans)
             {
               case -2:fout<<"Case #"<<count<<": Bad magician!";
                    break;
               case -3:fout<<"Case #"<<count<<": Volunteer cheated!";
                    break;
               default:fout<<"Case #"<<count<<": "<<ans;
                       break;
               
               }
    
    
    
    
    
    
    fin.close();
    fout.close();
    //cout<<endl;
    //system("PAUSE");
    return 0;
    
}
