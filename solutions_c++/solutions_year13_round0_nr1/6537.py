#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <cmath>
#include <fstream>
#include <set>
#include <map>
#include <iomanip>
#include <string>
#include <cstring>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <list>
#include <climits>
#include <cctype>
#include <bitset>

using namespace std;

int main()
{


    freopen("A-large.in", "rt", stdin);
    freopen("A-large.out", "wt", stdout);
   
    int z;
	cin >>z;
    string s;
    
//______________________________________________________________________
	for (int a=0 ; a <z;a++ ){
	vector<string>v;
	for (int i =0 ; i < 4 ; i++)
    {
		cin>>s;
		v.push_back(s);
	}
		
		bool Xwon=false;
		bool Owon=false;
		
    for (int i =0 ; i < 4 ; i++)
    {
		if ( count (v[i].begin(), v[i].end() , 'X') == 4 || (count (v[i].begin(), v[i].end() , 'X')==3 && count (v[i].begin(), v[i].end() , 'T')==1)  )
	    Xwon=true;
	    else if ( count (v[i].begin(), v[i].end() , 'O') == 4 || (count (v[i].begin(), v[i].end() , 'O')==3 && count (v[i].begin(), v[i].end() , 'T')==1)  )
	    Owon=true;
	    
	}
	for (int i =0 ; i < 4 ; i++)
    {
		string temp="";
		temp+=v[0][i];
		temp+=v[1][i];
		temp+=v[2][i];
		temp+=v[3][i];
		if ( count (temp.begin(), temp.end() , 'X') == 4 || (count (temp.begin(), temp.end() , 'X')==3 && count (temp.begin(),temp.end() , 'T')==1)  )
	    Xwon=true;
	    else if ( count (temp.begin(), temp.end() , 'O') == 4 || (count (temp.begin(), temp.end() , 'O')==3 && count (temp.begin(), temp.end() , 'T')==1)  )
	    Owon=true;
	   	
	}
	string temp="";
	for (int i =0 ; i <4 ; i++)
	temp+=v[i][i];
	if ( count (temp.begin(), temp.end() , 'X') == 4 || (count (temp.begin(), temp.end() , 'X')==3 && count (temp.begin(),temp.end() , 'T')==1)  )
    Xwon=true;
    else if ( count (temp.begin(), temp.end() , 'O') == 4 || (count (temp.begin(), temp.end() , 'O')==3 && count (temp.begin(), temp.end() , 'T')==1)  )
    Owon=true;
        temp="";
	 	temp+=v[0][3];
		temp+=v[1][2];
		temp+=v[2][1];
		temp+=v[3][0];
    if ( count (temp.begin(), temp.end() , 'X') == 4 || (count (temp.begin(), temp.end() , 'X')==3 && count (temp.begin(),temp.end() , 'T')==1)  )
    Xwon=true;
    else if ( count (temp.begin(), temp.end() , 'O') == 4 || (count (temp.begin(), temp.end() , 'O')==3 && count (temp.begin(), temp.end() , 'T')==1)  )
    Owon=true;
    //_________________________________________________________________________________________________
    string t=v[0]+v[1]+v[2]+v[3];
    if (!Xwon && !Owon &&(count (t.begin(), t.end() , 'O')+count (t.begin(), t.end() , 'X')+count (t.begin(), t.end() , 'T')==16 ))
    cout<<"Case #"<<a+1<<": Draw"<<endl;
     else if (Xwon)
    cout<<"Case #"<<a+1<<": X won"<<endl;
    else if (Owon)
    cout<<"Case #"<<a+1<<": O won"<<endl;
    else 
    cout<<"Case #"<<a+1<<": Game has not completed"<<endl;
    Xwon=Owon=false;
	}
    

return 0;
}

