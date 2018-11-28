#include <iostream>
#include <list>
using namespace std;
int worker(int r, int c, int x){
    if(x == 1)
        return 1;
    if(x == 2){
        if(r %2 != 0 && c %2 != 0)
            return 0;
        else   
            return 1;
    }
    if(x == 3)
    {
        if( r <=2 && c <=2  )
            return 0;
        if((r*c )%3 != 0)
            return 0;
        if( r == 1 || c == 1)
            return 0;
        return 1;
    }
    if(x == 4)
        if(r <=2 || c <=2 )
            return 0;
        if((r * c) %4 != 0)
            return 0;
        return 1;
}

int main(){
    int testCase;
    cin>>testCase;
    
    for(int i = 0; i< testCase ; i++){
        int r, c, x;
        cin>>x>>r>>c;
        if(worker(r, c, x) == 1)
             cout<<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
         else 
            cout<<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
    }

}