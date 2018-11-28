#include <iostream>
#include <fstream>
using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::ifstream;
using std::ofstream;

int main(void){
    ifstream in; // read input from file
    ofstream out; // write output to file

    string s;
    int T,n,standing,friends;


    in.open("input.txt");
    out.open("output.txt");

    /* number of test cases */
    in >> T;
    /* loop through test cases */
    for(int j=0;j<T;j++){
        in >> n;
        in >> s;
        standing = 0;
        friends = 0;

        //cout << "n: " << n << endl;
        //cout << "s: " << s << endl;

        for(int i=0;i<=n;i++){
            if(standing<i){
                friends+= i-standing;
                standing+= i-standing;
            }
            standing+= int(s[i]-'0');
            //cout << "standing: " << standing << endl;
        }
        //cout << "output: " << friends;

        /* write to output file */
        out << "Case #" << j+1 << ": " << friends << "\n";
    }
    /* close files */
    in.close();
    out.close();

    return 0;
}
