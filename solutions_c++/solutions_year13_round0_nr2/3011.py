#include "iostream"
#include "iomanip"
#include "vector"
#include "numeric"
#include <string>
#include "fstream"
#include "stdlib.h"
#include "algorithm"
#include "math.h"
using namespace std;


int main(){
    string str;
    int n,row,line,temp;

    fstream ifs("B-large.in",ios_base::in);
    fstream ofs("b.ou",ios_base::out);
    ifs>>n;
    for(int i=0;i<n;++i){
        ifs>>row>>line;
        vector<vector<int> > rect;

        for(int k=0;k<row;++k){
            vector<int> tmp;
            for(int j=0;j<line;++j){
                ifs>>temp;
                tmp.push_back(temp);
            }
            rect.push_back(tmp);
        }

        vector<int> rowMax(row,0);
        vector<int> lineMax(line,0);
        for(int k=0;k<row;++k){
            for(int j=0;j<line;++j){
                if(rowMax[k]<rect[k][j]){
                    rowMax[k]=rect[k][j];
                }
            }
            //ofs<<"row "<<k<<":"<<rowMax[k]<<endl;
        }
        for(int j=0;j<line;++j){
            for(int k=0;k<row;++k){
                if(lineMax[j] < rect[k][j]){
                    lineMax[j] = rect[k][j];
                }
            }
            //ofs<<"line "<<j<<":"<<lineMax[j]<<endl;
        }
        string out =  "YES";
        for(int j=0;j<line;++j){
            for(int k=0;k<row;++k){
                if(rect[k][j]<lineMax[j] && rect[k][j] <rowMax[k]){
                    out = "NO";
                    break;
                }
            }
        }
        ofs<<"Case #"<<i+1<<": "<<out<<endl;
    }
    ifs.close();
    ofs.close();
    return 0;
}

