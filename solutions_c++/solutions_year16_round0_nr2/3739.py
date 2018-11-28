#include<iostream>
#include<string>
#include<queue>
using namespace std;
int main()
{
    int T,maneuvers;
    string pancake_stack;
    string::iterator it;
    cin>>T;
    for(int i=0;i<T;i++){
        maneuvers=0;
        cin>>pancake_stack;
        it=pancake_stack.end()-1;
        while( *it == '+')it--;
        pancake_stack.erase(++it,pancake_stack.end());
        if(!pancake_stack.empty()){
            maneuvers += 1;
            it = pancake_stack.begin();
            while(it != --pancake_stack.end()){
                if(*it != *(++it))maneuvers += 1;
            }
        }
        cout<<"Case #"<<i+1<<": "<<maneuvers<<endl;
    }
}
