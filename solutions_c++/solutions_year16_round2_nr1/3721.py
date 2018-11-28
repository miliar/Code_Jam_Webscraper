#include <bits/stdc++.h>

using namespace std;
#define ll long long
vector< pair<string, int> > glo ;
string ans, glos ;
bool letsDoTheShit(string str1, string str2)
{
    //cout << str1 << " " << str2 << endl ;
    sort(str1.begin(), str1.end()) ;
    sort(str2.begin(), str2.end()) ;
    //cout << str1 << " " << str2 << endl ;
    if(str1==str2)
        return true ;
    else
        return false ;
}

void rec(int i, int rem, string actual)
{
    //cout << i << " " << rem << " " << actual << endl ;
    if(rem==0)
    {
        string temp ;
        for(int i=0;i<actual.size();i++)
        {
            if(actual[i]=='0')
                temp += "ZERO" ;
            if(actual[i]=='1')
                temp += "ONE" ;
            if(actual[i]=='2')
                temp += "TWO" ;
            if(actual[i]=='3')
                temp += "THREE" ;
            if(actual[i]=='4')
                temp += "FOUR" ;
            if(actual[i]=='5')
                temp += "FIVE" ;
            if(actual[i]=='6')
                temp += "SIX" ;
            if(actual[i]=='7')
                temp += "SEVEN" ;
            if(actual[i]=='8')
                temp += "EIGHT" ;
            if(actual[i]=='9')
                temp += "NINE" ;
        }
        //cout << actual << " " << temp << endl ;
        if(letsDoTheShit(temp, glos))
            ans = actual ;
        return ;
    }
    if(rem<0||i>=glo.size())
        return ;
    for(int j=0;j<=glo[i].second;j++)
    {
        string temp = actual ;
        for(int k=0;k<j;k++)
        {
            if(glo[i].first=="ZERO")
                temp.push_back('0') ;
            if(glo[i].first=="ONE")
                temp.push_back('1') ;
            if(glo[i].first=="TWO")
                temp.push_back('2') ;
            if(glo[i].first=="THREE")
                temp.push_back('3') ;
            if(glo[i].first=="FOUR")
                temp.push_back('4') ;
            if(glo[i].first=="FIVE")
                temp.push_back('5') ;
            if(glo[i].first=="SIX")
                temp.push_back('6') ;
            if(glo[i].first=="SEVEN")
                temp.push_back('7') ;
            if(glo[i].first=="EIGHT")
                temp.push_back('8') ;
            if(glo[i].first=="NINE")
                temp.push_back('9') ;
        }
        rec(i+1, rem-(glo[i].first.size()*j), temp) ;
    }
}

int makeString(string str, vector<char> vect)
{
    int ret = 0 ;
    for(int i=0;i<str.size();i++)
    {
        bool found = 0 ;
        for(int j=0;j<vect.size();j++)
        {
            if(vect[j]==str[i])
            {
                found = 1 ;
                vect.erase(vect.begin()+j) ;
                break ;
            }
        }
        if(!found)
            break ;
        if(i==str.size()-1)
        {
            ret++ ;
            i = -1 ;
        }
    }
    return ret ;
}

int main()
{
    ios_base::sync_with_stdio(0) ;
    freopen("A-small-attempt2.in","r",stdin) ;
    freopen("A-small-attempt2.out","w",stdout) ;
    int t, cs = 1 ;
    cin >> t ;
    while(t--)
    {
        string str ;
        cin >> str ;
        glos = str ;
        map<string, vector<char> > mym ;
        vector<string> numbers {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"} ;
        for(int i=0;i<str.size();i++)
        {
            for(int k=0;k<numbers.size();k++)
            {
                for(int j=0;j<numbers[k].size();j++)
                {
                    if(numbers[k][j]==str[i])
                    {
                        mym[numbers[k]].push_back(str[i]) ;
                        break ;
                    }
                }
            }
        }
        for(map<string, vector<char> >::iterator it=mym.begin();it!=mym.end();it++)
        {
            int x = makeString(it->first, it->second) ;
            if(it->first=="ZERO"&&x!=0)
                glo.push_back(make_pair("ZERO", x)) ;
            if(it->first=="ONE"&&x!=0)
                glo.push_back(make_pair("ONE", x)) ;
            if(it->first=="TWO"&&x!=0)
                glo.push_back(make_pair("TWO", x)) ;
            if(it->first=="THREE"&&x!=0)
                glo.push_back(make_pair("THREE", x)) ;
            if(it->first=="FOUR"&&x!=0)
                glo.push_back(make_pair("FOUR", x)) ;
            if(it->first=="FIVE"&&x!=0)
                glo.push_back(make_pair("FIVE", x)) ;
            if(it->first=="SIX"&&x!=0)
                glo.push_back(make_pair("SIX", x)) ;
            if(it->first=="SEVEN"&&x!=0)
                glo.push_back(make_pair("SEVEN", x)) ;
            if(it->first=="EIGHT"&&x!=0)
                glo.push_back(make_pair("EIGHT", x)) ;
            if(it->first=="NINE"&&x!=0)
                glo.push_back(make_pair("NINE", x)) ;
        }
        /*for(int i=0;i<glo.size();i++)
        {
            cout << glo[i].first << " " << glo[i].second << endl ;
        }*/
        rec(0, str.size(), "") ;
        sort(ans.begin(), ans.end()) ;
        cout << "Case #" << cs << ": " << ans << "\n" ;
        cs++ ;
        glo.clear() ;
        ans.clear() ;
    }

    return 0;
}
