#include <bits/stdc++.h>

using namespace std;

string wArr[13] = {
                    "ZERO","ONE","TWO",
                    "THREE","FOUR","FIVE",
                    "SIX","SEVEN", "EIGHT" , "NINE",
                    };

string wNum;


bool fn(int curNum , string curW)
{
    string tmpW = curW;
    string fnVal = wArr[curNum];
    for(int ct = 0; ct < fnVal.size(); ct++)
    {
        if(tmpW.find(fnVal[ct]) == string::npos)
        {
            return false;//curW.erase(curW.find(fnVal[ct]));
        }
        else
        {
            tmpW.erase(tmpW.find(fnVal[ct]) , 1);
        }
    }
    return true;
}

string delW(int curNum , string curWt)
{
    string tmpW = curWt;
    string fnVal = wArr[curNum];
    for(int ct = 0; ct < fnVal.size(); ct++)
    {
        //if(curW.find(fnVal[ct]) == string::npos)
        {
            tmpW.erase(tmpW.find(fnVal[ct]) , 1);
        }
    }
    return tmpW;

}

string vcToCh(vector<char>& vcCh)
{
    string ret = "";
    for(int ctc = 0; ctc < vcCh.size(); ctc++)
    {
        ret += vcCh[ctc];
    }
    return ret;
}
bool ft;
void get(string curWNum, vector<char>& retVal)
{
    if(curWNum == "")
    {
        cout << vcToCh(retVal) << endl;
        ft = true;
        return;
    }
    if(ft)
        return;
    for(int ct = 0; ct <= 9; ct++)
    {
        if(fn(ct , curWNum))
        {
            string tmpV = curWNum;
            curWNum = delW(ct , curWNum);
            retVal.push_back(ct+'0');
            get(curWNum , retVal);
            retVal.pop_back();
            curWNum = tmpV;
        }
        if(ft)
            break;
    }
    //cout << ret << endl;
}

int main()
{
    int tetC;
    cin >> tetC;
    for(int cnt = 0; cnt < tetC; cnt++)
    {
        ft = false;
        cin >> wNum;
        cout << "Case #" << cnt+1 << ": ";
        vector<char> retVc;
        get(wNum , retVc);

    }
    return 0;
}
