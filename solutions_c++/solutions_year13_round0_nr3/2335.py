#include<iostream>
#include<sstream>
#include<vector>
#include<string>
using namespace std;

bool isPalindromes(const string& pstr)
{
    int n=pstr.length();
    if(n==1) return true;
    for(int i=0; i<n/2; ++i)
    {
        if(pstr[i]!=pstr[n-i-1])
        {
            return false;
        }
    }
    return true;
}
string stringAdd(const string& str1, const string& str2)
{
    string ret = "";
    int i=str1.length()-1;
    int j=str2.length()-1;
    int p = 0;
    while(i>=0 || j>=0)
    {
        int ui = 0;
        if(i>=0){
            char ci = str1[i];        
            ui = ci-'0';
        }

        int uj = 0;
        if(j>=0)
        {
            char cj = str2[j];
            uj = cj-'0';
        }
        int nv = ui+uj+p;
        p = nv/10;
        int nn = nv%10;
        char nc = nn+'0';
        string ns;
        ns.push_back(nc);
        ret = ns + ret;
        if(i>=0) --i;
        if(j>=0) --j;
    }
    if(p>0){
        ret = "1" + ret;
    }
    return ret;
}
string strSquare(const string& rtStr)
{

    unsigned int v = strtoul(rtStr.c_str(), NULL, 0);
    string result = "0";
    int az=-1;
    for(int i=rtStr.length()-1; i>=0; --i)
    {
        ++az;
        char c = rtStr[i];
        int u = c-'0';
        int mul = 0;
        if(u==0)
        {
            continue;
        }
        else if(u==1)
        {
            mul = v;
        }
        else
        {
            mul = v*u;
        }
        char buf[80]={0};
        itoa(mul, buf, 10);
        string ss = buf;
        for(int z=0; z<az; ++z)
        {
            ss.append("0");
        }
        result=stringAdd(result, ss);

    }
    return result;
}
bool strGreatEquThen(const string& str1, const string& str2)
{
    if(str1.length() > str2.length()) return true;
    if(str1.length() < str2.length()) return false;
    for(int i=0; i<str1.length(); ++i)
    {
        if(str1[i]==str2[i]) continue;
        if(str1[i]>str2[i]) return true;
        if(str1[i]<str2[i]) return false;
    }
    return true;
}
int _tmain(int argc, _TCHAR* argv[])
{
    
    vector<string> sqrSet;
    vector<int> lenvec;
    //for(int i=1; i<10000000; ++i)
    for(int i=1; i<3000000; ++i)        
    //for(int i=1; i<10000; ++i)
    {
        ostringstream convert;
        convert << i;
        string istr = convert.str();
        if(isPalindromes(istr))
        {
            string tmp = strSquare(istr);
            if(tmp.size()>14) break;
            if(isPalindromes(tmp))
            {
                sqrSet.push_back(tmp);
                lenvec.push_back(tmp.size());
                //cout << tmp << endl;
            }
        }
    }
    int cN;
    cin >> cN;
    for(int ci=0; ci<cN; ++ci)
    {
        string s, e;
        cin >> s >> e;
        int si = 0;
        for(int i=0; i<lenvec.size(); ++i)
        {
            //cout << s.length() << ", " << lenvec[i] << endl;
            if(s.length() <= lenvec[i])
            {
                si=i;
                break;
            }
        }
        int cnt = 0;
        for(int i=si; i<lenvec.size(); ++i)
        {
            if(lenvec[i] > e.length())
            {
                break;
            }
            if(strGreatEquThen(sqrSet[i], s) && strGreatEquThen(e, sqrSet[i]))
            {
                ++cnt;
            }
        }
        printf("Case #%d: %d\n", ci+1, cnt);
        
    }
	return 0;
}

