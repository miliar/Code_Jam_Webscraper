#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>
#include <unistd.h>


using namespace std;

vector<int> v1;
vector<int> v2;
int total = -1;
int result=-1;
int counts=4;
int item=-1;

int main(int argc,char **argv){
    ifstream inf;

    inf.open(argv[1]);

    if(!inf.good())
        return -1;

    inf >> total;
    cout << "total: " << total << endl;
    cout << "counts: " << counts << endl;
    string str;
    for( int i = 0; i < total; i ++ ) {
        v1.clear();
        v2.clear();
        int row1;
        inf >> row1;
        cout << "row1: "<< row1 << endl;
  
        for( int o = 0; o < counts; o ++) {
            /*if( row1 != (o+1)){
                getline(inf, str);
                cout << "line " << str << " discarded" << endl;
                continue;
            }*/
            //cout << "o = " << o << endl;
            for( int j = 0; j < counts; j ++) {
                inf >> item;
                //cout << "\titem: " << item << endl;
                if( row1 == (o+1))
                    v1.push_back(item);
            }
        }
        int row2;
        inf >> row2;
        cout << "row2: "<< row2 << endl;
 
        for( int o = 0; o < counts; o ++) {
            /*if( row2 != (o+1)){
                getline(inf, str);
                cout << "line " << str << " discarded" << endl;
                continue;
            }*/
            //cout << "o = " << o << endl;
            for( int j = 0; j < counts; j ++) {
                inf >> item;
                //cout << "\titem: " << item << endl;
                if( row2 == (o+1))
                    v2.push_back(item);
            }
        }
        cout << "-------------" << endl;

        //sort(v1.begin(), v2.end());
        //sort(v2.begin(), v2.end());

        cout << "v1: ";
         for( int a = 0; a < counts; a++ ) 
            cout << " " << v1.at(a);
        cout << endl;
        
        cout << "v1: ";
         for( int a = 0; a < counts; a++ ) 
            cout << " " << v2.at(a);
        cout << endl;
  
        int value = -1;
        int found = 0;
        //cout << "Case " << i << ": " << endl; 
        for(int k = 0; k < v1.size(); k++) {
                cout << "finding col1: " << k << " item = " << v1.at(k) << endl;
                //cout << "v2 content: ";
                //for(int m = 0; m < counts; m++ )
                 //   cout << v2.at(m) << " ";
                //cout << endl;
                //vector<int>::iterator it = find( v2.begin(), v2.end(), v1.at(k) );
                for( int s = 0; s < v2.size(); s++ ) {
                if( v1.at(k) == v2.at(s) ){
                    //cout << "value " << v1.at(k) << " not find in vector" << endl;
                //} 
                //else {
                    found++;
                    value = v1.at(k);
                    cout << ">>>>>> found in v2" << endl;
                }
                }
        }
        switch( found ) {
            case 0: 
                cout << "Case #" << (i+1) << ": Volunteer cheated!" << endl;
                break;
            case 1: 
                cout << "Case #" << (i+1) << ": " << value << endl;
                break;
            default:
                cout << "Case #" << (i+1) << ": " << "Bad magician!" << endl;
        cout << "-------------" << endl;
    }
    }

    return 0;
}
