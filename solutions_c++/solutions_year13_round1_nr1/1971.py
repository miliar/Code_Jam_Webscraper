//
//  rings.c
//  
//
//  Created by Abdallah on 4/26/13.
//
//
#include <fstream>
#include <iostream>

using namespace std;

main()
{
    ifstream fin;
    ofstream fout;
    
    fin.open("data.in.txt");
    fout.open("data.out.txt");
    
    int T,r,t,i,j;
    fin >> T;
    cout<<T;
    for(i=0;i<T;i++)    //iteration for each case
    {
        fin>>r>>t;
        int rem=t;
        int rings=0;
        for(j=0;;j+=2)
        {
            int req=2*(r+j)+1;
            if(rem>=req)
            {
                rings++;
                rem=rem-req;
            }
            else
                break;
            
        }
        fout<<"Case #"<<i+1<<": "<<rings<<endl;

        
        
    }
    fin.close();
    fout.close();
}