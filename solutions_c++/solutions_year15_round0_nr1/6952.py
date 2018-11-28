//
//  main.cpp
//  A
//
//  Created by JAY PATEL on 4/10/15.
//  Copyright (c) 2015 JAY PATEL. All rights reserved.
//

#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    freopen("/Users/JAY/desktop/gcj/a/input.txt", "r", stdin);
    freopen("/Users/JAY/desktop/gcj/a/output.txt", "w", stdout);
    int tt;
    cin >> tt;
    for (int qq = 1; qq <= tt; qq++) {
        int smax;
        scanf("%d",&smax);
        int persons[smax+1];
        int totalper = 0;
            string line;
            cin>>line;
            for(int k=0;k<=smax;k++){
                persons[k] = line[k]-48;
                totalper=totalper+persons[k];
            }
        int count=0;
        int j=0;
        for(int i=smax;i>=0;i--){
            totalper = totalper - persons[i];
            if(totalper < i){
                int toadd = i-totalper;
                count=count+toadd;
                while(toadd>0){
                    while(persons[j]<9&&toadd>0){
                        persons[j]++;
                        totalper++;
                        toadd--;
                    }
                    if(toadd>0)
                        j++;
                }
            }
        }
        cout <<"Case #"<<qq<<": "<<count<<endl;
    }
    return 0;
}
