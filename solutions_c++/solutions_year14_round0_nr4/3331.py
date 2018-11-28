/*
 * purpose: a template backbone for CodeJam solution
 * created: 2014-03-15
 * revised: 2014-03-29
 * author: Hoffman Tsui
 * 
 * start time: 18:19
 * end time: 11:00
 * think till time: 19:02
 * pause at 19:27
 * resume at 21:22
 * test passed at 23:32
 * time to completion: n min(s)
 */

#include <unistd.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <list>
#include <algorithm>


void help();

namespace TMP {
    template<class T>
    struct reverse {
        bool operator()(T const &a, T const &b) {
            return b < a;
        }
    };
};

void print (const std::list<float> & q) {
    std::cout<<"print elements" << std::endl;
    for ( auto & it : q ) {
        std::cout << it << std::endl;        
    }
}
int war (int N, std::list<float> n, std::list<float> k) {
    // given sorted as big to small weights
    int n_mark = 0;
    while (N>0) {
        std::list<float>::iterator nit = --n.end();
        std::list<float>::iterator kit = --k.end();
        float b_v = *nit;
        n.pop_back();
        if (b_v > *kit) {
        // k's lose strategy
            float tmp = *n.begin(); 
            k.pop_front();
            //std::cout << "b_v = " << b_v << ", lose with = " << tmp << std::endl;
            n_mark++;
        } else {
        // win strategy 
            kit = std::upper_bound(k.begin(), k.end(), b_v);
            //kit--; //point to the slightly bigger than b_v;
            //std::cout << "b_v = " << b_v << ", win by = " << *kit << std::endl;
            k.erase(kit);
        }
        N--;
    }
    return n_mark;
}

// all wk < all wn, N
// all wk > all wn, 0
// intention to pass as a copy
int dwar (int N, std::list<float> n, std::list<float> k) {
    // given sorted as small to big weights
    int n_mark = 0;
    std::list<float>::iterator nit = n.begin();
    std::list<float>::iterator kit = k.begin();
    // n's deceitful lose strategy
    while (*nit < *kit) {
        float s_v = *nit;
        float tmp = *(--k.end()); 
        k.pop_back();
        n.pop_front();
        nit = n.begin();
        kit = k.begin();
        //std::cout << "s_v = " << s_v << ", lose for = " << tmp << std::endl;
    }
    int M = n.size();
    for (int i=0; i<M; i++) {
        std::list<float>::iterator nit = --n.end();
        std::list<float>::iterator kit = --k.end();
        float b_v = *nit;
        if (b_v > *kit) {
            // n's win strategy
            float tmp = *n.begin(); 
            n.pop_back();
            k.pop_back();
            //std::cout << "b_v = " << b_v << ", lose with = " << tmp << std::endl;
            n_mark++;
        } else {
            // deceitful lose strategy 
            n.pop_front();
            k.pop_back();
        }
        //print(n);
        //print(k);
    }
        
    //n_mark = M;
    //std::cout << n_mark << std::endl;
    return n_mark;
}

int main (int argc, char *argv[]) {
    int c;
    const char* in_file;
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
        int T;
        int N;
        is >> T;
        for (int c=1; c<=T; c++) {
            std::list<float> nw, kw;
            is >> N; 
            for (int n=1; n<=N; n++) {
                float w;
                is >> w;
                nw.push_back(w);
            }
            for (int n=1; n<=N; n++) {
                float w;
                is >> w;
                kw.push_back(w);
            }

            nw.sort();
            kw.sort();
            //print(nw);
            //print(kw);
            int points = dwar(N, nw, kw);
            cout << "Case #" << c << ": " << dwar(N, nw, kw) << " " << war(N, nw, kw) << endl;
        }
    }
	is.close();

	return 0;
}

void help() {
    std::cerr << "Usage: command [-f filename]" << std::endl;
}
