#include<iostream>
#include<cstdlib>
#include<vector>
using namespace std;
int main(){
    freopen("test2.txt","r",stdin);
     freopen("out.txt","w",stdout);
    int n,f,s,temp;
  
    cin>>n;
    for(int j=0;j<n;j++){
        vector<int>chosen1;
        vector<int>chosen2;
        vector<int>res;
        cin>>f;
        for(int i=0;i<4;i++){
            for(int k=0;k<4;k++){
                cin>>temp;
                if(i+1==f){
                    chosen1.push_back(temp);
                }        
            }
        }
        cin>>s; 
        for(int i=0;i<4;i++){
            for(int k=0;k<4;k++){
                cin>>temp;
                if(i+1==s){
                    chosen2.push_back(temp);
                }        
            }
        }
        bool bad=false;
        for(int i=0;i<4;i++){
            for(int k=0;k<4;k++){
                if(chosen1[i]==chosen2[k]){
                    res.push_back(chosen1[i]);
                    if(res.size()==2){
                        bad=true;
                        break;
                    }        
                }
            }
            if(bad)
                break;
        }
        if(bad)
            cout<<"Case #"<< j+1 <<": Bad magician!"<<endl;
        else if(res.size()==1)
            cout<<"Case #"<<j+1 <<": "<< res[0]<<endl;
        else
            cout<<"Case #"<< j+1 <<": Volunteer cheated!"<<endl;
        
    }
    return 0;
}
