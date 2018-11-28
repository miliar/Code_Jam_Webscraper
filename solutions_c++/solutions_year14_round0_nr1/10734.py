#include <stdio.h>
#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <list>
#include <stack>
#include <algorithm>
#include <iterator>
#include <sstream>
#include <string>
#include <cmath>
#include <math.h>

using namespace std;
//string --> int
int sti (const string &s){
    int x;
    stringstream ss(s);
    ss>>x;
    return x;
}
//int --> string
string its (const int &x){
    string s;
    stringstream ss(s);
    ss<<x;
    s=ss.str();
}

//Scan String using scanf
void sscan(string &str){
	str = ""; //clear string

	char str_c;
	scanf( "%c" , &str_c );

	//stop scan if there is space or new line
	while(!(str_c=='\n'||str_c==' ')){
        str += str_c;
        scanf( "%c" , &str_c );
    }
}

//Print String using printf
void sprint(const string &str){
	int length = str.length();
	for(int i=0; i<length; ++i)
        printf("%c",str[i]);
}

int main()
{/*
#ifndef ONLINE_JUDGE
    freopen ( "input.txt","rt",stdin );	//Read Input From File
    freopen ("output.txt","wt",stdout);	//Put Output In File
#endif*/

    //Input
    int TEST;
    scanf("%d",&TEST);

    for(int ii=1; ii<=TEST; ++ii){
        //which row her card is in before and after
        int ans1,ans2;
        set<int> set1;
        int set2[4];
        scanf("%d",&ans1);
        int x;
        for(int i=1; i<5; ++i)
        for(int j=1; j<5; ++j){
            scanf("%d",&x);
            if(i == ans1){
                set1.insert(x);
            }
        }
        scanf("%d",&ans2);
        for(int i=1; i<5; ++i)
        for(int j=0; j<4; ++j){
            scanf("%d",&x);
            if(i == ans2){
                set2[j]=x;
            }
        }
        //---------------

        int coun=0;
        for(int i=0; i<4; ++i){
            if(set1.count(set2[i])){
                x=set2[i];
                coun++;
            }
        }

        //----------------
        if(coun==1)
            printf("Case #%d: %d\n",ii,x);
        else if(coun==0)
            printf("Case #%d: Volunteer cheated!\n",ii);
        else
            printf("Case #%d: Bad magician!\n",ii);


    }


/*

#ifndef ONLINE_JUDGE
    fclose(stdin);
    fclose(stdout);
#endif*/
    return 0;

}
