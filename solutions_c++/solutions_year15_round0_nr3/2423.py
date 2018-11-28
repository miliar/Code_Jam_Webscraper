#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>

using namespace std;

class quat
{
    enum base {null, mk, mj, mi, m1, p1, pi, pj, pk};
    base v;
    void convert(base v, int& i, base& w);
    void iconvert(int i, base v, base& w);
    base multiply(base i, base j);
public:
    quat operator *(quat i);
    quat operator -();
    bool operator ==(quat i);
    void set1() { v = p1; }
    void seti() { v = pi; }
    void setj() { v = pj; }
    void setk() { v = pk; }
};

void quat::convert(quat::base v, int& i, quat::base& w)
{
    switch(v)
    {
    case mk:
	w = pk;
	i = -1;
	break;
    case mj:
	w = pj;
	i = -1;
	break;
    case mi:
	w = pi;
	i = -1;
	break;
    case m1:
	w = p1;
	i = -1;
	break;
    case pk:
    case pj:
    case pi:
    case p1:
	i = 1;
	w = v;
	break;
    default:
	abort();
    }
}	

void quat::iconvert(int i, quat::base v, quat::base& w)
{
    if (i == 1)
    {
	w = v;
	return;
    }
    switch(v)
    {
    case pk:
	w = mk;
	break;
    case pj:
	w = mj;
	break;
    case pi:
	w = mi;
	break;
    case p1:
	w = m1;
	break;
    case mk:
	w = pk;
	break;
    case mj:
	w = pj;
	break;
    case mi:
	w = pi;
	break;
    case m1:
	w = p1;
	break;
    default:
	abort();
    }
}

quat::base quat::multiply(quat::base i, quat::base j)
{
    if (i == p1)
	switch(j)
	{
	case p1:
	    return p1;
	case pi:
	    return pi;
	case pj:
	    return pj;
	case pk:
	    return pk;
	default:
	    abort();
	}
    if (i == pi)
	switch(j)
	{
	case p1:
	    return pi;
	case pi:
	    return m1;
	case pj:
	    return pk;
	case pk:
	    return mj;
	default:
	    abort();
	}
    if (i == pj)
	switch(j)
	{
	case p1:
	    return pj;
	case pi:
	    return mk;
	case pj:
	    return m1;
	case pk:
	    return pi;
	default:
	    abort();
	}
    if (i == pk)
	switch(j)
	{
	case p1:
	    return pk;
	case pi:
	    return pj;
	case pj:
	    return mi;
	case pk:
	    return m1;
	default:
	    abort();
	}
    abort();
    return null;
}

quat quat::operator *(quat i)
{
    quat res;
    int li, ri;
    base l, r;
    convert(v, li, l);
    convert(i.v, ri, r);
    base val = multiply(l, r);
    iconvert(li * ri, val, res.v);
    return res;
}

quat quat::operator -()
{
    quat res;
    int i;
    base val;
    convert(v, i, val);
    i *= -1;
    iconvert(i, val, res.v);
    return res;
}

bool quat::operator ==(quat i)
{
    return v == i.v;
}

quat q[20000];

int main()
{
    quat p1, pi, pj, pk;
    p1.set1();
    pi.seti();
    pj.setj();
    pk.setk();
    int t, l, x;
    string s;
    cin >> t;
    for (int cases = 1; cases <= t; cases++)
    {
	cin >> l >> x >> s;
	quat ansl = p1;
	for (int i = 0; i < l; i++)
	{
	    switch(s[i])
	    {
	    case 'i':
		q[i] = pi;
		break;
	    case 'j':
		q[i] = pj;
		break;
	    case 'k':
		q[i] = pk;
		break;
	    }
	    ansl = ansl * q[i];
	}
	quat ans = p1;
	for (int i = 0; i < x; i++)
	    ans = ans * ansl;
	quat m1 = -p1;
	cout << "Case #" << cases << ": ";
	if (!(ans == m1))
	{
	    cout << "NO" << endl;
	    continue;
	}
	ans = p1;
	bool succl = false;
	int posli, poslj;
	for (int i = 0; i < 16 && i < x; i++)
	    for (int j = 0; j < l && !succl; j++)
	    {
		ans = ans * q[j];
		if (ans == pi)
		{
		    posli = i;
		    poslj = j;
		    succl = true;
		}
	    }
	ans = p1;
	bool succr = false;
	int posri, posrj;
	for (int i = 0; i < 16 && i < x; i++)
	    for (int j = l - 1; j >= 0 && !succr; j--)
	    {
		ans = q[j] * ans;
		if (ans == pk)
		{
		    posri = i;
		    posrj = j;
		    succr = true;
		}
	    }
	if (succl && succr)
	{
	    if (posli < x - 1 - posri ||
		(posli == x - 1 - posri && poslj + 1 < posrj))
	    {
		if (posli < x - 1 - posri)
		{
		    ans = p1;
		    for (int j = poslj + 1; j < l; j++)
			ans = ans * q[j];
		    for (int j = posli + 1; j < x - 1 - posri; j++)
			ans = ans * ansl;
		    for (int j = 0; j < posrj; j++)
			ans = ans * q[j];
		    if (ans == pj)
			cout << "YES" << endl;
		    else
			cout << "FUCK" << endl;
		}
		else
		{
		    ans = p1;
		    for (int j = poslj + 1; j < posrj; j++)
			ans = ans * q[j];
		    if (ans == pj)
			cout << "YES" << endl;
		    else
			cout << "FUCK" << endl;
		}
	    }
	    else cout << "NO" << endl;
	}
	else
	    cout << "NO" << endl;
    }
}
