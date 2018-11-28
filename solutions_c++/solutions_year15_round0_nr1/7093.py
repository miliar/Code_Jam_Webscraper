#include <iostream>

using namespace std;

int main(){
    int loops;
    cin>>loops;
    for(int l=1; l<loops+1;l++){
        string audience, drop;
        int standing=0;
        int additional=0;
        cin>>drop;
        cin>>audience;
        for(int i=0;i<audience.size();i++){
            if(audience[i]=='0' || standing>=i){
                standing+=(audience[i]-'0');
            }
            else{
                additional+=(i-standing);
                standing=i;
                standing+=(audience[i]-'0');
            }
        }
        cout<<"Case #"<<l<<": "<<additional<<endl;
    }
    return 0;
}
