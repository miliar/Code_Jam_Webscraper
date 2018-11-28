#include <iostream>
#include <algorithm>
#include <list>

using namespace std;


int main()
{
    int t, *a;

    cin>>t;
    a = new int[t];

    for(int i=0; i<t; i++)
        cin>>a[i];

    for(int i=0; i<t; i++){
        int j=1;
        list<int> l;
        int c = 0;
        int n;
        if(a[i]==0){
            cout<<"Case #1: INSOMNIA"<<endl;
            continue;
        }
        while(1){
            n = j*a[i];
            while(n!=0){
                list<int>::iterator f = find (l.begin() , l.end(), n%10);
                if(f==l.end()){
                    l.push_back(n%10);
                    c++;
                }
                n/=10;
            }
            j++;
            if(c == 10){
                break;
            }
        }
        cout<<"Case #"<<i+1<<": "<<(j-1)*a[i]<<endl;
    }
    return 0;
}
