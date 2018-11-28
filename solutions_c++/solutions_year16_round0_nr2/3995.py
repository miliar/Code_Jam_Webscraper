#include <bits/stdc++.h>
using namespace std;
string whatevs;
map <string,int> distances;
typedef pair <int,string> pi;
typedef priority_queue <pi,vector <pi>,greater <pi> > pq;
pq dijkstras;
string alpha;
string beta;
map <char,char> complements;
string flip(string stuff){
    string other = "";
    for(int i =0;i<stuff.size();i++){
        other += complements[stuff[stuff.size()-1-i]];
    }
    return other;
}
set <string> seen;
int main()
{
    complements['+'] = '-';
    complements['-'] = '+';
    int n;
    freopen("pancake.in","r",stdin);
    freopen("pancake.out","w",stdout);
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        seen.clear();
        distances.clear();
        cin >> whatevs;
        string best = "";
        for(int j = 0;j<whatevs.size();j++){
            best += '+';
        }
        while(!dijkstras.empty() )
            dijkstras.pop();
        dijkstras.push(make_pair(0,whatevs));
        distances[whatevs] = 0;
        seen.insert(whatevs);
        while(!dijkstras.empty()){
            pi cur = dijkstras.top();
            dijkstras.pop();
            string mine = cur.second;
            int dist = cur.first;
            if(mine == best){
                cout << "CASE" << " " << "#" << i+1 << ":" << " " << dist << endl;
                break;
            }
            for(int j=0;j<mine.size();j++){
                //cout << mine << endl;
                alpha = mine.substr(0,j+1);
                beta = mine.substr(j+1);
                alpha = flip(alpha);
                //cout << alpha << endl;
                string mm = (string)(alpha+beta);
                //cout << mm << endl;
                if(seen.count(mm)){
                    //cout << mm << endl;
                   if(dist + 1 < distances[mm]){
                        distances[mm] = dist + 1;
                        dijkstras.push(make_pair(distances[mm],mm));
                    }
                }
                else{
                    //cout << mm < endl;
                    distances[mm] = dist + 1;
                    seen.insert(mm);
                    dijkstras.push(make_pair(distances[mm],mm));
                }
            }
        }
    }
    return 0;
}
