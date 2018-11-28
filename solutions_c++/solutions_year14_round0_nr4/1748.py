#include<fstream>
#include<iostream>
#include<sstream>
#include<vector>
#include<algorithm>
using namespace std;

long long war(vector<double> naomi, vector<double> ken){
    long long score=0;
    for(int i=0;i<naomi.size();i++){
        if(ken[0]<naomi[i]){ // all ken less than naomi[i]
            ken.pop_back(); // use the smallest one
            score++; // naomi wins
        }
        else if(naomi[i]<ken.back()) // all ken greater than naomi[i]
            ken.pop_back(); // use the smallest one
        else{
            int j=-1;
            while(naomi[i]<ken[j+1]) j++;
            ken.erase(ken.begin()+j);
        }

    }
    return score;
}

long long dwar(vector<double> naomi, vector<double> ken){
    long long score=0;
    for(int i=0;i<ken.size();i++){
        if(naomi.back()<ken[i]){ // all naomi smaller than ken[i]
            break;
        }
        else{
            int j=0;
            while(naomi[j]<ken[i]) j++;
            score++; // naomi wins
            naomi.erase(naomi.begin()+j); // use naomi[j]
        }
    }
    return score;
}

int main(){
    ifstream infile("D-large.in");
    ofstream outfile("D-large.out");
    string line;
    getline(infile,line);
    int T,t=1;
	istringstream is(line);
	is>>T;
	is.clear();

	while(t<=T){
	    getline(infile,line);
	    is.str(line);
        int n;
        is>>n;
        is.clear();

        vector<double> naomi(n,0), ken(n,0);
        //read Naomi's
        getline(infile,line);
        is.str(line);
        for(int i=0;i<n;i++)    is>>naomi[i];
        is.clear();

        //read Ken's
        getline(infile,line);
        is.str(line);
        for(int i=0;i<n;i++)    is>>ken[i];
        is.clear();

        sort(naomi.begin(),naomi.end(),greater<double>());
        sort(ken.begin(),ken.end(),greater<double>());
        long long warscore=war(naomi,ken);

        reverse(naomi.begin(),naomi.end());
        reverse(ken.begin(),ken.end());
        long long dwarscore=dwar(naomi,ken);

        outfile<<"Case #"<<t<<": "<<dwarscore<<" "<<warscore<<endl;

		t++;
	}
	infile.close();
	outfile.close();

    return 0;
}
