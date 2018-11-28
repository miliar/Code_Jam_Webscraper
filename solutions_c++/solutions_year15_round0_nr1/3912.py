#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

int main(){
	string filename1 = "A-large.in";
	ifstream infile(filename1.c_str());
	string filename2 = "out2.txt";
	ofstream outfile(filename2.c_str());
    int T;
    infile>>T;
    for(int k = 1; k <= T; k++){
        int s_max;
        infile>>s_max;
        string str;
        infile>>str;
        int Num_people_added = 0;
        int Num_people_current = 0;
        Num_people_current = static_cast<int>(str[0] - '0');
        for(int i = 1; i <= s_max; i++){
            if(i > Num_people_current){
                Num_people_added = Num_people_added > (i-Num_people_current)? Num_people_added : (i-Num_people_current);
            }
             Num_people_current += static_cast<int>(str[i] - '0');
        }
        outfile<<"Case #"<<k<<": "<<Num_people_added<<endl;
    }
	infile.close();
    outfile.close();
    return 0;
}
