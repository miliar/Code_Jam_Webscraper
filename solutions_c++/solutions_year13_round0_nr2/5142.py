#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {

    int i =0;
    int j =0;
    int k =0;
    int l =0;
        
    int cases = 0;
    cin >> cases;
    
    const int size = 100;
    int lawn[size][size];
    for(i=0; i<cases; i++)
    {
        int N = 0;
        int M = 0;
        int a = 0;
        
        int failed = 0;
        cin>>N>>M;
        for(j=0; j<N; j++)
        {
            for(k=0; k<M; k++)
            {
                cin>>lawn[j][k];
            }
        }
        for( j=0; j<N; j++)
        {
            for(k=0; k<M; k++)
            {
                int hor = 0;
                int ver = 0;
                for(l=0; l<N; l++)
                {
                    if(lawn[l][k]>lawn[j][k])
                    {
                        hor = 1;
                    }
                    
                }
                for(l=0; l<M; l++)
                {
                    if(lawn[j][l]>lawn[j][k])
                    {
                        ver = 1;
                    }
                }
                if((hor==1)&&(ver==1))
                {
                    failed = 1;
                    break;
                }
            }
            
            if(failed == 1)
            {
                break;
            }
        }
        cout<<"Case #"<<i+1<<": ";
        if(failed == 1)
        {
            cout<<"NO"<<endl;
        }
        else if(failed == 0)
        {
            cout<<"YES"<<endl;
        }
    }
    return 0;
}