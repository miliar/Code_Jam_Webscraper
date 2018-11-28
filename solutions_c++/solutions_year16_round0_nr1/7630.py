#include <string>
#include <iostream>
#include <vector>
using namespace std;


int main(){

    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int temp;
        cin>>temp;
        if (temp == 0)
        {
            cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
            continue;
        
        }
        int j=1;
        int *exist = (int *)calloc(10,sizeof(int));
        while(1){
            int temp2=j*temp;
            string str = to_string(temp2);
            for(int k=0;k<str.length();k++)
            {
                if(!exist[str[k]-'0'])
                    exist[str[k]-'0'] = 1;
            
            }
            int tmpbool = 1;
            for(int k=0;k<10;k++)
                tmpbool &= exist[k];
            if(tmpbool == 1){
                cout<<"Case #"<<i+1<<": "<<temp2<<endl;
                
                break;
            }
            j++;
        }
        
        
    
    }



}
