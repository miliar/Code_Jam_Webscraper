#include <bits/stdc++.h>
using namespace std;
int main()
{
        int T;
        cin>>T;
        int t;
        for(t=1;t<=T;t++)
        {
                vector <int> v1;
                vector <int> v2;
                int N;
                cin>>N;
                int array[4][4];
                memset(array,0,sizeof(array));
                int i,j;
                for(i=0;i<4;i++)
                {
                        for(j=0;j<4;j++)
                        {
                                cin>>array[i][j];
                                if(N==i+1)
                                        v1.push_back(array[i][j]);
                                             
                        }
                }
                
                
                cin>>N;
                memset(array,0,sizeof(array));
                
                for(i=0;i<4;i++)
                {
                        for(j=0;j<4;j++)
                        {
                                cin>>array[i][j];
                                if(N==i+1)
                                        v2.push_back(array[i][j]);
                        }
                }
                int ans=0;
                int flag=0;
                int to_print=-1;
                for(i=0;i<4;i++)
                {
                        for(j=0;j<4;j++)
                        {
                             if(v1[i]==v2[j])
                             {
                                ans++;
                             }
                                
                             if (ans==1 && flag==0)
                             {
                                to_print=v1[i];  
                                flag=1;
                             }
                                
                                                  
                        }
                }
                if(ans==0)
                        cout<<"Case #"<<t<<": "<<"Volunteer cheated!"<<endl;
                else if(ans==1)
                        cout<<"Case #"<<t<<": "<<to_print<<endl;
                else
                        cout<<"Case #"<<t<<": "<<"Bad magician!"<<endl;
        }
        
        return 0;
}

