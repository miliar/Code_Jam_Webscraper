#include<fstream>
#include<sstream>
#include<set>
using namespace std;

int main(){
    ifstream infile("A-small-attempt0.in");
    ofstream outfile("A-small-attempt0.out");
    string line;
    getline(infile,line);
    int T,t=1;
	istringstream is(line);
	is>>T;

	while(t<=T){
	    getline(infile,line);
	    istringstream is1(line);
        int r1,r2;
        is1>>r1;
        set<int> s;
        for(int i=0;i<4;i++){
            getline(infile,line);
            if(i+1!=r1) continue;
            istringstream is2(line);
            for(int j=0;j<4;j++){
                int temp;
                is2>>temp;
                s.insert(temp);
            }
        }

        getline(infile,line);
        istringstream is3(line);
        is3>>r2;
        int record=0;
        bool bad_mag=false;
        for(int i=0;i<4;i++){
            getline(infile,line);
            if(i+1!=r2) continue;
            istringstream is4(line);
            for(int j=0;j<4;j++){
                int temp;
                is4>>temp;
                if(s.find(temp)!=s.end()){
                    if(record==0){
                        record=temp;
                    }
                    else{
                        outfile<<"Case #"<<t<<": Bad magician!"<<endl;
                        bad_mag=true;
                        break;
                    }
                }
            }
            if(record==0)
                outfile<<"Case #"<<t<<": Volunteer cheated!"<<endl;
            else if(!bad_mag)
                outfile<<"Case #"<<t<<": "<<record<<endl;
        }
		t++;
	}
	infile.close();
	outfile.close();

    return 0;
}
