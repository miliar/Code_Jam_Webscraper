#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <queue>
#include <array>
#include <set>
#include <string>


/*

"ZERO" -> z.
"ONE" --> o.
"TWO" -> w.
"THREE" --> h.
"FOUR" -> u.
"FIVE" --> f.
"SIX" -> x.
"SEVEN" --->v.
"EIGHT" -> g.
"NINE" 

*/


using namespace std;

void solve(string str){
    multiset<int> number;
    int pos;
    // zero
    while((pos = str.find_first_of('Z'))!=-1){
        //cout<<"zero";
        str.erase(pos, 1);
        int e = str.find_first_of('E');
        str.erase(e, 1);
        int r = str.find_first_of('R');
        str.erase(r, 1);
        int o = str.find_first_of('O');
        str.erase(o, 1);
        number.insert(0);
    }
    
    // two
    while((pos = str.find_first_of('W'))!=-1){
        //cout<<"two";
        str.erase(pos, 1);
        int t = str.find_first_of('T');
        str.erase(t, 1);
        int o = str.find_first_of('O');
        str.erase(o, 1);
        number.insert(2);
    }
    
    // four
    while((pos = str.find_first_of('U'))!=-1){
        str.erase(pos, 1);
        int f = str.find_first_of('F');
        str.erase(f, 1);
        int o = str.find_first_of('O');
        str.erase(o, 1);
        int r = str.find_first_of('R');
        str.erase(r, 1);
        number.insert(4);
    }
    
    // six
     while((pos = str.find_first_of('X'))!=-1){
        str.erase(pos, 1);
        int s = str.find_first_of('S');
        str.erase(s, 1);
        int i = str.find_first_of('I');
        str.erase(i, 1);
        number.insert(6);
    }
    
    // eight
    while((pos = str.find_first_of('G'))!=-1){
        str.erase(pos, 1);
        int e = str.find_first_of('E');
        str.erase(e, 1);
        int i = str.find_first_of('I');
        str.erase(i, 1);
        int h = str.find_first_of('H');
        str.erase(h, 1);
        int t = str.find_first_of('T');
        str.erase(t, 1);
        number.insert(8);
    }
    
    // one
    while((pos = str.find_first_of('O'))!=-1){
        str.erase(pos, 1);
        int n = str.find_first_of('N');
        str.erase(n, 1);
        int e = str.find_first_of('E');
        str.erase(e, 1);
        number.insert(1);
    }
    
    // three
    while((pos = str.find_first_of('H'))!=-1){
        str.erase(pos, 1);
        int t = str.find_first_of('T');
        str.erase(t, 1);
        int r = str.find_first_of('R');
        str.erase(r, 1);
        int e = str.find_first_of('E');
        str.erase(e, 1);
        e = str.find_first_of('E');
        str.erase(e, 1);
        number.insert(3);
    }
    
    // five
    while((pos = str.find_first_of('F'))!=-1){
        str.erase(pos, 1);
        int i = str.find_first_of('I');
        str.erase(i, 1);
        int v = str.find_first_of('V');
        str.erase(v, 1);
        int e = str.find_first_of('E');
        str.erase(e, 1);
        number.insert(5);
    }
    
    // seven
    while((pos = str.find_first_of('V'))!=-1){
        str.erase(pos, 1);
        int s = str.find_first_of('S');
        str.erase(s, 1);
        int e = str.find_first_of('E');
        str.erase(e, 1);
        e = str.find_first_of('E');
        str.erase(e, 1);
        int n = str.find_first_of('N');
        str.erase(n, 1);
        number.insert(7);
    }
    
    // nine
    while(str.length()!=0){
        int n = str.find_first_of('N');
        str.erase(n, 1);
        int i = str.find_first_of('I');
        str.erase(i, 1);
        n = str.find_first_of('N');
        str.erase(n, 1);
        int e = str.find_first_of('E');
        str.erase(e, 1);
        number.insert(9);
    }
    
    for (multiset<int>::iterator it=number.begin(); it!=number.end(); ++it){
        cout<<*it;
    }
    cout<<endl;
}

int main(){
    int n;
    cin>>n;
    for(int i=1; i<=n; ++i){
        string str;
        cin>>str;
        cout<<"Case #"<<i<<": ";
        solve(str);
    }
    return 0;
}