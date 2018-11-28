#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{

#ifndef ONLINE_JUDGE
	freopen("a2.in", "rt", stdin);
	freopen("a2.out", "wt", stdout);
#endif

int nb;
cin>>nb;

for(int i=0;i<nb;i++){

    string ligne;
    cin>>ligne;
     cout<<"Case #"<<i+1<<": ";
     /*
        sort(ligne.begin(),ligne.end());
        reverse(ligne.begin(),ligne.end());*/
        string li ;
        li.push_back(ligne[0]);
        for(int j=1; j<=ligne.length()-1;j++){

            if(li[0] > ligne[j]){

                li = li+ligne[j];
            }
            else
            li = ligne[j]+li;

        }
        cout<<li<<endl;

}

    return 0;
}
