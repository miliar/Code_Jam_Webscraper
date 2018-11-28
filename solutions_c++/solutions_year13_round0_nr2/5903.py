//
//  main.cpp
//  gcj
//
//  Created by Milo Brandt on 4/13/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <fstream>
#include <iostream>
#include <map>

int main (int argc, const char * argv[])
{
    std::string x;
    std::cout << "Filename: ";
    std::cin >> x;
    std::ifstream in(x.c_str());
    std::ofstream out("/Users/Milo/Documents/boobs.txt");
    if(!in.is_open()){
        std::cout << "Macs suck.\n";
        return EXIT_FAILURE;
    }
    int trials;
    in >> trials;
    std::getline(in, x);
    for(int t = 1;t <= trials;++t){
        bool ans = true;
        int N,M;
        in >> N;
        in >> M;
        int* tab = new int[N*M];
        for(int i = 0;i< N*M;++i){
            in >> tab[i];
        }
        for(int x = 0; x < M;++x){
            for(int y = 0; y < N;++y){
                int val = tab[y*M+x];
                bool onegood = true;
                for(int x2 =0;x2 < M;++x2){
                    if(tab[y*M+x2]>val){
                        onegood = false;
                        break;
                    }
                }
                if(onegood) continue;
                for(int y2 =0;y2 < N;++y2){
                    if(tab[y2*M+x]>val){
                        ans = false;
                        goto finale;
                    }
                }
            }
        }
    finale:
        out << "Case #" << t << ": " << (ans?"YES":"NO") << std::endl;
        delete[] tab;
    }
    out.close();
    in.close();
    return 0;
}

