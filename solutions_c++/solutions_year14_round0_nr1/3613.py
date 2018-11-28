#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream min ("MA.in");
    ofstream mout ("Magic_Trick_result.txt");
    int t;
    min>>t;
    for(int l=0;l<t;l++)
    {
            
            int a,total=0,found;
            min>>a;
            int ar[4][4];
            for(int i=0;i<4;i++)
            {
                    for(int j=0;j<4;j++)
                    {
                            
                            min>>ar[i][j];
                            }
                    }
                    int b;
                    min>>b;
                    int ar1[4][4];
            for(int i=0;i<4;i++)
            {
                    for(int j=0;j<4;j++)
                    {
                            min>>ar1[i][j];
                            }
                    }

                    
                    
                    
                    



                    
                    for(int i=0;i<4;i++)
                    {
                            for(int j=0;j<4;j++)
                            {
                                  //  cout<<ar1[b-1][i]<<" "<<ar[a-1][j]<<endl;
                                    if(ar1[b-1][i]==ar[a-1][j])
                                    {
                                                           
                                                           found=ar1[b-1][i];
                                    //                       cout<<found;
                                                           total++;
                                                           }
                                    }
                                    
                            }
                    //cout<<endl;        
                    if(total==1)
                    mout<<"Case #"<<l+1<<": "<<found<<endl;
                    else if (total==0)
                    mout<<"Case #"<<l+1<<": Volunteer cheated!"<<endl;
                    else
                    mout<<"Case #"<<l+1<<": Bad magician!"<<endl;
            
            }
            min.close();
            mout.close();
            //system("pause");
    return 0;
}
