#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <algorithm>


#define For(i,n) for(int i(0),_n(n);i<_n;++i)

using namespace std;


int main(int argc, char const *argv[]) {
    long long T;
    fstream f("in.in");
    f >> T;
    For(t,T) {
        long long M,N;
        int h;
        f >> N;
        f >> M;
        set<int> heights;
        vector<vector<int> > lawn;

        For(i,N) {
            vector<int> vect;
            For(j,M){
                f >> h;
                if(heights.find(h) == heights.end())
                    heights.insert(h);
                vect.push_back(h);
            }
            lawn.push_back(vect);
        }

        for(set<int>::iterator iter = heights.begin(); iter != heights.end(); ++iter) {
            For(i,N) {
                For(j,M){
                    if(lawn[i][j] == *iter) {
                        bool hor=true,ver=true;
                        For(k,N) {
                            if(lawn[k][j]>*iter)
                                ver=false;
                        }
                        For(q,M) {
                            if(lawn[i][q]>*iter)
                                hor=false;
                        }

                        if(!hor && !ver) {
                            cout << "Case #" << t+1 << ": NO" << endl;
                            goto stop;
                        }
                    }
                }
            }
        }
        cout << "Case #" << t+1 << ": YES" << endl;
        stop:;
    }
    f.close();
    return 0;
}
