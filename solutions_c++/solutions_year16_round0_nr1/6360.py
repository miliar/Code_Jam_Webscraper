#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    ifstream cin("A-large.in");
    ofstream cout("largeOutput.txt");

    int tc, i, n, j, mult, aux;
    set<int> numbers;
    cin>>tc;
    i=1;
    while(i<=tc){
        numbers.clear();
        cin>>n;
        cout<<"Case #"<<i<<": ";
        if(n==0){
            cout<<"INSOMNIA\n";
        }else{
            j=1;
            while(numbers.size()<10){
                mult=n*j;

                aux=mult;
                while(aux>0){
                    numbers.insert(aux%10);
                    aux/=10;
                }
                j++;
            }

            cout<<mult<<"\n";
        }
        i++;
    }
    return 0;
}
