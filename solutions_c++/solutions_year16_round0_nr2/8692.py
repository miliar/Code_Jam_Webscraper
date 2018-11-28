#include<iostream>
#include<stack>
using namespace std;
int change = 0;
int check(stack<char> a,int ss){
    change++;
    int c = 0;
    while(!a.empty()){
            if(a.top()!= '+') return 0;
            a.pop();
            c++;
    }
    if(c==ss) return 1;
    else return 0;

}
int main(){
    int t,m=1;
    for(cin>>t;t--;){
        stack <char> s,temp;
        string x;
        cin>>x;
        char y;
        for(int i=x.length()-1;i>=0;i--){
            s.push(x[i]);

        }
        while(!check(s,s.size())){
           y = s.top();

           while(!s.empty()){
                if(s.top()!=y) break;
                 s.pop();
                temp.push(u);

           }
           if(y=='+'){
                u = '-';
           }
           else u = '+';


           while(!temp.empty()){
                temp.pop();
                s.push(u);
           }
        }

        cout<<"Case #"<<m<<": "<<change-1<<endl;
        change = 0;
        m++;

    }



    return 0;
}
