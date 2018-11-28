#include <bits/stdc++.h>
using namespace std;


int main()
{

    ifstream in("input.txt");
    ofstream out("output.txt");
#define cin in
#define cout out


    int nbCas;
    cin>>nbCas;

    for(int c=1;c<=nbCas;c++) {
        cout<<"Case #"<<c<<": ";
        int N;
        cin>>N;
        int sum = 0;
        priority_queue<pair<int,int> > pq;
        for(int c=0;c<N;c++){
            int z;
            cin>>z;
            sum+=z;
            pq.push(make_pair(z,c));
        }
        while(pq.size()) {
            if(pq.size() == 2 && pq.top().first == 2) {
                pair<int,int> one = pq.top();
                pq.pop();
                pair<int,int> two = pq.top();
                pq.pop();
                if(two.first == 1) {
                    cout<<(char)(one.second+'A')<<" ";
                    one.first--;
                    sum--;
                    pq.push(one);
                    pq.push(two);
                }
                else {
                    cout<<(char)(one.second+'A')<<(char)(two.second+'A')<<" ";
                    one.first--;
                    two.first--;
                    sum--;
                    sum--;
                    pq.push(one);
                    pq.push(two);
                }
            }
            else {
                pair<int,int> one  = pq.top();
                pq.pop();
                one.first--;
                sum--;
                cout<<(char)(one.second+'A');
                if(one.first != 0) {
                    pq.push(one);
                }
                if(pq.size() && (sum+1)%2==0){
                    pair<int,int> two = pq.top();
                    pq.pop();
                    two.first--;
                    sum--;
                    cout<<(char)(two.second+'A');
                    if(two.first!=0) {
                        pq.push(two);
                    }
                }
                cout<<" ";
            }
        }
        cout<<endl;
    }



}
