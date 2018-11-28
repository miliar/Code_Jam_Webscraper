#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <iostream>


using namespace std;
struct column {
    int idx;
    int sum; // # of L's
    bool operator<(const column& other) const { // for priority queue
        return sum > other.sum;
    }
};


void printTiles(vector<string> tiles){
    for(int i=0; i<tiles.size(); ++i){
        cout<<tiles[i]<<endl;
    }
}

vector<string> genK(vector<string> &tiles, string str, int k, int counter){
    // generates possible k's
    if(counter==k){
        tiles.push_back(str);
        //cout<<str<<endl;
    } else {
        genK(tiles, str+'G', k, counter+1);
        genK(tiles, str+'L', k, counter+1);
    }
    return tiles;
}

vector<string> calcTiles(vector<string> originals, int k, int c){
    // generates possible kc's
    int v_size = originals.size();
    vector<string> tiles = originals;
    vector<string> last;
    
    while(--c){ // cause I want it to stop at 1
        last = tiles;
        int len = last[0].length();
        for(int i=0; i<v_size; ++i){
            string line;
            for(int j=0; j<len; ++j){
                if(last[i][j]=='L'){
                    line.append(originals[i]);
                } else {
                    for(int l=0; l<k; ++l)
                        line.push_back('G');
                } 
            }
            tiles[i] = line;
            //cout<<tiles[i]<<endl;
        }
    }
    //cout<<endl<<"total: "<<tiles[0].length()<<endl;
    
    return tiles;
}

void genResult(vector<string> tiles, int s){
    vector<int> indxs;
    priority_queue<column> cols;
    int size = tiles.size();
    int len = tiles[0].length();
    //cout<<size<<endl;
    //printTiles(tiles);
    for(int col=0; col<len; ++col){
        int sum = 0;
        for(int row=0; row<size-1; ++row){
            // cout<<"row: "<<row <<"col: "<<col<<endl;
            if(tiles[row][col]=='L'){
                ++sum;
                //cout<<row<<":"<<col<<" sum: "<<sum<<endl;
            }
              
        }
        //cout<<sum<<endl;
        column current;
        current.sum = sum;
        current.idx = col;
        cols.push(current);
    }
    // while(!cols.empty()){
    //     cout<<cols.top().idx<<" : "<<cols.top().sum<<endl;

    //     // cout<<cols.top().idx<<" ";
    //     cols.pop();
    // }

    column init = cols.top();
    cols.pop();
    int diff = init.sum;
    int lpos;
    for(int row=0; row<tiles.size()-1; ++row){
        if(tiles[row][init.idx]=='L'){
            lpos = row;
        }
    }
    int found = 0;
    if(diff==0)
        cout<<" "<<init.idx+1<<endl;
    else if(diff!=0 &&s>=2){
        cout<<" "<<init.idx+1;
        while(!cols.empty()&&found==0){
            column current = cols.top();   cols.pop();
            
            for(int row=0; row<tiles.size()-1; ++row){
                if(tiles[row][current.idx]=='L'&& row!=lpos){
                    cout<<" "<<current.idx+1<<endl;
                    
                    //cout<<(float)current.idx/tiles[0].length()*100<<"%"<<endl;
                    found = 1;
                    break;
                }
            }
        }
    } else {
        cout<<"IMPOSSIBLE"<<endl;
    }
}
int main(){
    int n, k, c, s, i;
    scanf("%d", &n);
    
    for(i=1; i<=n; ++i){
        scanf("%d %d %d", &k, &c, &s);
        vector<string> tiles;
        cout<<"Case #"<<i<<":";
        if(k==1){
            cout<<" "<<1<<endl;
        } else if(k!=s){
            tiles = genK(tiles,"", k, 0);
            tiles = calcTiles(tiles, k,c);
            
            //cout<<endl;
            //printTiles(tiles);
            genResult(tiles, s);
        } else if(c==1 && k==s){
            for(int pos0=0; pos0<k; ++pos0){
                cout<<" "<<pos0+1;   
            }
            cout<<endl;
        } else { // k==s
            //cout<<"else"<<endl;
            long long offset =  pow(k, c-1);
            long long idx = 0;
            for(int pos0=0; pos0<k; ++pos0){
                //cout<<"c: "<<c<< endl;
                cout<<" "<<idx+pos0+1;
                idx+=offset;
            }
            cout<<endl;
        }
    }
    return 0;
}
