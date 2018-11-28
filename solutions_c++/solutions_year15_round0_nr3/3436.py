#include <iostream>
#include <string>

using namespace std;

int L,X;
//bool sign;

string superstring;

/*string compact(string s, bool b)
{
    string res = "";
    char t;
    unsigned int j;
    unsigned int i=0,repeat;
    sign = b;
    while(i<s.length())
    {
        t = s[i];
        j=i+1;
        while((j<s.length()) && (s[j]==t)) j++;
        if (j-i==2)
        {
            sign = !sign;
            repeat = 1;
        }
        else if (j-i>4)
        {
            repeat = (j-i)%4;
        }
        else repeat = j-i;
        for(unsigned int z=1;z<=repeat;z++) res += t;
        i=j;
    }
    L=res.length();
    return res;
}*/

void expand(string s)
{
    superstring = "";
    //if ((s.length()==1) && (X>4)) X %=4;
    /*s = compact(s,true);
    cout << "S = " << s << endl;*/
    for(int i=1;i<=X;i++) superstring = superstring + s;
    /*superstring = compact(superstring,sign);*/
}

char compute(char x, char y)
{
    if ((x=='1') && (y=='1')) return '1';
    if ((x=='1') && (y=='i')) return 'i';
    if ((x=='1') && (y=='j')) return 'j';
    if ((x=='1') && (y=='k')) return 'k';
    if ((x=='i') && (y=='1')) return 'i';
    if ((x=='i') && (y=='i')) return '0'; //-1
    if ((x=='i') && (y=='j')) return 'k';
    if ((x=='i') && (y=='k')) return 'J'; //-j
    if ((x=='j') && (y=='1')) return 'j';
    if ((x=='j') && (y=='i')) return 'K'; //-k
    if ((x=='j') && (y=='j')) return '0'; //-1
    if ((x=='j') && (y=='k')) return 'i';
    if ((x=='k') && (y=='1')) return 'k';
    if ((x=='k') && (y=='i')) return 'j';
    if ((x=='k') && (y=='j')) return 'I'; //-i
    if ((x=='k') && (y=='k')) return '0'; //-1
    return 'x';
}

bool computesign(bool x, bool y)
{
    if ((x) && (y)) return true;
    else if ((x) && (!y)) return false;
    else if ((!x) && (y)) return false;
    else if ((!x) && (!y)) return true;
    return false;
}

bool check(int i, int j, char c, bool b)
{
    char t='1';
    bool sign = b;
    bool csign;
    for(int k=i;k<=j;k++)
    {
        t = compute(t,superstring[k]);
        csign=true;
        if (t=='0')
        {
            t = '1';
            csign = false;
        }
        else if (t=='I')
        {
            t = 'i';
            csign = false;
        }
        else if (t=='J')
        {
            t = 'j';
            csign = false;
        }
        else if (t=='K')
        {
            t = 'k';
            csign = false;
        }
        sign = computesign(sign,csign);
    }
    if ((t==c) && (!sign)) return true;
    return false;
}

int index(int start, int last, char c)
{
    int i=start;
    char t='1';
    bool b = true,csign;
    while(i<=superstring.length()-1)
    {
        t = compute(t,superstring[i]);
        csign=true;
        if (t=='0')
        {
            t = '1';
            csign = false;
        }
        else if (t=='I')
        {
            t = 'i';
            csign = false;
        }
        else if (t=='J')
        {
            t = 'j';
            csign = false;
        }
        else if (t=='K')
        {
            t = 'k';
            csign = false;
        }
        b = computesign(b,csign);
        if ((i>last) && (t==c) && (b)) return i;
        i++;
    }
    return -1;
}

bool solve()
{
    if (L*X<3) return false;
    //if ((L*X==3) && (superstring[0]=='i') && (superstring[1]=='j') && (superstring[2]=='k')) return true;
    /*for(unsigned int i=1;i<superstring.length()-2;i++)
    {
        for(unsigned int j=i+1;j<superstring.length()-1;j++)
        {
            if ((sign==true) && (check(0,i-1,'i',true)) && (check(i,j-1,'j',true)) && (check(j,superstring.length()-1,'k',true))) return true;
            else if ((sign==false) && (check(0,i-1,'i',true)) && (check(i,j-1,'j',true)) && (check(j,superstring.length()-1,'k',false))) return true;
            else if ((sign==false) && (check(0,i-1,'i',true)) && (check(i,j-1,'j',false)) && (check(j,superstring.length()-1,'k',true))) return true;
            else if ((sign==false) && (check(0,i-1,'i',false)) && (check(i,j-1,'j',true)) && (check(j,superstring.length()-1,'k',true))) return true;
        }
    }
    return false;*/
    //for(unsigned int i=0;i<superstring.length()-2;i++)
    if (!check(0,superstring.length()-1,'1',true)) return false;
    int indi,indj,indk,lindi,lindj,lindk;
    indi=-1;indj=-1;indk=-1;
    while(true)
    {
        indi=index(0,indi,'i');
        if (indi!=-1)
        {
            indj=index(indi+1,indj,'j');
            if (indj!=-1)
            {
                indk=index(indj+1,indk,'k');
                if (indk!=-1) return true;
            }
        }
        else return false;
    }
}

int main()
{
    int T;
    cin >> T;
    string s;
    for(int z=1;z<=T;z++)
    {
        cin >> L >> X;
        cin >> s;
        expand(s);
        if (solve()) cout << "Case #" << z << ": " << "YES" << endl;
        else cout << "Case #" << z << ": " << "NO" << endl;
    }
    return 0;
}
