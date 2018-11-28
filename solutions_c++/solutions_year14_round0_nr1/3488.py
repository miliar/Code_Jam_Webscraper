/*
 * purpose: a template backbone for CodeJam solution
 * created: 2014-03-15
 * revised: 2014-03-29
 * author: Hoffman Tsui
 * 
 * start time: 9:23 
 * end time: 11:00
 * read time: 9:30
 * pause at :10:05, resumed: 10:39
 * passed test sample: 10:56 
 * time to completion: n min(s)
 */

#include <unistd.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <map>
#include <algorithm>

const int N=4;
int fR[4];
int sR[4];

void print(int * arr) {
    std::cout << "You got a row:" << std::endl;
    for (int j=0; j<N; j++) {
       std::cout << arr[j] << " " ;
    }
    std::cout <<  std::endl;
}

void get_row(std::ifstream& fin, int t, int* arr) {
    using namespace std;
    string line;
    for (int i=1; i<=N; i++) {
        getline(fin,line);
        if (i==t) {
           stringstream ss; 
           ss << line;
           for (int j=0; j<N; j++) {
               ss >> arr[j];
           }
        }
    }
    //print(arr);
}

std::string magic(int* farr, int* narr) {
    // count the occurence
    std::string res = "";
    std::map<int, int> ctr;
    for (int i=0; i<N; i++) {
        ctr[farr[i]]++;
        ctr[narr[i]]++;
    }
    if (ctr.size() == N*2) {
        res = "Volunteer cheated!";
    } else if (ctr.size() < N*2-1) {
        res = "Bad magician!";
    } else if (ctr.size() == N*2-1) {
        std::map<int,int>::iterator it;
        for (it=ctr.begin(); it!=ctr.end(); it++) {
            if ((it->second) == 2) {
                std::stringstream ss;
                ss << (it->first);
                ss >> res;
            }
        }
    }
    return res;
}

void help();

int main (int argc, char *argv[]) {
    int c;
    const char* in_file;
    //const char* out_file;
    while (( c = getopt(argc, (char **)argv, "f:h:?")) != -1) {
        char flag = (char)c;
        switch(flag) {
            case 'f':
                in_file = optarg;
                break;
            default:
                help();
        }
    }
    
    // declar data structure
    
    // read content from file, close the stream when finish
    std::ifstream is(in_file);
	if (!is) {
		return 2;
    } else {
        // load into data structure
        using namespace std;
        string line;
        int T;
        is >> T;
        for (int c=1; c<=T; c++) {
            int F,N;
            is >> F;
            getline(is, line);
            get_row(is, F, fR);
            is >> N;
            getline(is, line);
            get_row(is, N, sR);
            cout << "Case #" << c << ": " << magic(fR, sR) << endl;
        }
    }
	is.close();

	return 0;
}

void help() {
    std::cerr << "Usage: command [-f filename]" << std::endl;
}
