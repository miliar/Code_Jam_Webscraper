#include <stdio.h>
#include <string.h>
#include <string>
#include <iostream>
#include "similarity.h"
#include "utility.h"
#include <time.h>
#include <math.h>
#include <algorithm>

using namespace std;
int totSentence;
char s[1000];
struct Sentence
{
	int ti;
	int totword;
	string word[300];
	void print()
	{
		for (int i = 0; i < totword; ++i)
		{
			cout << word[i] << ' ';
		}
		cout << endl;
	}
}sen[2000];
void del(char s[])
{
	int l, len = strlen(s);
	for (l = 0; s[l] && s[l] != ' '; ++l);
	while (s[l] == ' ' && s[l + 1] == ' ') l++;
	for (int i = l + 1; i <= len; ++i)
	{
		s[i - l - 1] = s[i];
	}
}
void solve(int index, char s[])
{
	int len = strlen(s);
	int sec;
	sscanf(s, "%d", &sec);
	//printf("%s %d\n", s, sec);
	sen[index].ti = sec;
	del(s);
	sen[index].totword = 0;
	char tmp[300];
	while (s[0] != 0)
	{
		sscanf(s, "%s", tmp);
		sen[index].word[sen[index].totword++] = tmp;
		del(s);
	}

}
map <string, int> num;
void weight_init()
{
	FILE *f;
	f = fopen("word.txt", "r");
	int tmp;
	char st[200];
	string smp;
	for (int i = 0; i < 14629; ++i)
	{
		fscanf(f, "%*d %s %d %*lf %*lf", st, &tmp);
		smp = st;
		num[smp] = tmp;
	}
	fclose(f);
}
double weight(string s)
{
	return 1.0 - log(num[s] + 1) / log(20000000 + 1.0);
}
double senSim(Sentence s1, Sentence s2)
{
	map <string, bool> mp;
	mp.clear();
	int allword = 0;
	string tmpword[400];
	for (int i = 0; i < s1.totword; ++i)
	{
		if (!mp[s1.word[i]])
		{
			tmpword[allword++] = s1.word[i];
			mp[s1.word[i]] = true;
		}
	}
	for (int i = 0; i < s2.totword; ++i)
	{
		if (mp[s2.word[i]] == false)
		{
			tmpword[allword++] = s2.word[i];
			mp[s2.word[i]] = true;
		}
	}
	double svec1[400], svec2[400];
	int rvec1[400], rvec2[400];
	for (int i = 0; i < allword; ++i)
	{
		svec1[i] = 0;
		rvec1[i] = 0;
		for (int j = 0; j < s1.totword; ++j)
		{
			if (tmpword[i] == s1.word[j])
			{
				svec1[i] = 1 * weight(tmpword[i]) * weight(tmpword[i]);
				rvec1[i] = j + 1;
				break;
			}
			else
			{
				double dis = WordSimilarity::instance()->calc(tmpword[i], s1.word[j]) * weight(s1.word[j]) * weight(tmpword[i]) ;
				if (dis > svec1[i] && dis > 0.20)
				{
					svec1[i] = dis;
					rvec1[i] = j + 1;
				}
			}
		}
        svec2[i] = 0;
        rvec2[i] = 0;
		for (int j = 0; j < s2.totword; ++j)
		{
			if (tmpword[i] == s2.word[j])
			{
				svec2[i] = 1 * weight(tmpword[i]) * weight(tmpword[i]);
				rvec2[i] = j + 1;
				break;
			}
			else
			{
				double dis = WordSimilarity::instance()->calc(tmpword[i], s2.word[j]) * weight(s2.word[j]) * weight(tmpword[i]);
				if (dis > svec2[i] && dis > 0.20)
				{
					svec2[i] = dis;
					rvec2[i] = j + 1;
				}
			}
		}
	}
	double t1 = 0, t2 = 0, t3 = 0, r1 = 0, r2 = 0, r3 = 0, ss = 0, sr = 0;
	for (int i = 0; i < allword; ++i)
	{
		t1 += svec1[i] * svec2[i];
		t2 += svec1[i] * svec1[i];
		t3 += svec2[i] * svec2[i];
		r1 += pow(rvec1[i] - rvec2[i], 2.0);
		r2 += pow(rvec1[i] + rvec2[i], 2.0);
	}
	ss = t1 / (sqrt(t2) * sqrt(t3));
	sr = 1.0 - sqrt(r1) / sqrt(r2);
	double x = s1.totword, y = s1.totword;
	double res = 4.0 * x * y / (x * x + y * y + 2.0 * x * y);
	return (ss * 0.85 + sr * 0.15) * res;
}
FILE * f;
int totnode;
int tot1, tot2, list1[2000], list2[2000];
bool v[2000];
struct Graph
{
	int totedge;
	int head[200000];
	int to[200000];
	int next[200000];
	double weight[200000];
	void init()
	{
		memset(head, -1, sizeof(head));
		memset(weight, 0, sizeof(weight));
		totedge = 0;
	}
	void __addedge (int u, int v, double tmpweight)
	{
        to[totedge] = v;
		next[totedge] = head[u];
		weight[totedge] = tmpweight;
		head[u] = totedge++;
	}
	void addedge(int u, int v, double tmpweight)
	{
	    __addedge(u, v, tmpweight);
	    __addedge(v, u, tmpweight);
	}
	void dfs1(int u)
	{
	    list1[tot1++] = u;
	    v[u] = true;
		for (int i = head[u]; ~i; i = next[i])
		{
			int tv = to[i];
			if (!v[tv]) dfs1(tv);
		}
	}
    void dfs2(int u)
	{
	    list2[tot2++] = u;
	    v[u] = true;
		for (int i = head[u]; ~i; i = next[i])
		{
			int tv = to[i];
			if (!v[tv]) dfs2(tv);
		}
	}
}graph;
struct Edge
{
    int x,y;
    double weight;
}edge[100000];
int totedge;
double mp[2000][2000];
int father[2000], totp[2000];
bool cmp(Edge x, Edge y)
{
    return x.weight > y.weight;
}
char s1[300], s2[300];
int getfather(int x)
{
    if (father[x] == x) return father[x];
    return father[x] = getfather(father[x]);
}
bool check(int tot1, int tot2, double weight)
{
    double avg = 0, totv = 0;
    for (int i = 0; i < tot1; ++i)
    {
        for (int j = 0; j < tot2; ++j)
        {
            totv += mp[list1[i]][list2[j]];
        }
    }
    avg = totv / (tot1 * tot2);
    return (weight * 0.7 + avg * 0.3) > 0.35;

}
void dfs(int u)
{
    v[u] = true;
    printf("%d ", u);
    for (int i = graph.head[u]; ~i; i = graph.next[i])
    {
        int tv = graph.to[i];
        if (!v[tv]) dfs(tv);
    }
}
int main()
{
	freopen("ina.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	while (gets(s))
	{
		solve(totSentence++, s);
	}

	if (!WordSimilarity::instance()->init())
	{
		util::log("[ERROR] init failed!!");
		return 1;
	}
	weight_init();
	graph.init();

    for (int i = 0; i < totSentence; ++i)
    {
        for (int j = i - 1; j >= 0; --j)
        {
            if (sen[i].ti - sen[j].ti > 45) break;
            double t1 = senSim(sen[i], sen[j]);
			double t2 = (sen[i].ti - sen[j].ti) / (-60.0);
			double tmp = t1 * exp(t2);
			if (tmp < 0.3) continue;
            edge[totedge].x = i;
            edge[totedge].y = j;
            edge[totedge++].weight = tmp;
        }
        father[i] = i;
        totp[i] = 1;
    }
    sort(edge, edge + totedge, cmp);
    printf("%d\n", totedge);
    for (int i = 0; i < totedge; ++i)
    {
        //printf("%d %d %f\n", edge[i].x, edge[i].y, edge[i].weight);
        int fax = getfather(edge[i].x);
        int fay = getfather(edge[i].y);
        //printf("%d %d\n", fax, fay);
        if (fax != fay)
        {
            memset(v, 0, sizeof(v));
            tot1 = tot2 = 0;
            graph.dfs1(fax);
            graph.dfs2(fay);
            bool can;
            if (totp[edge[i].x] == 1 || totp[edge[i].y] == 1)
            {
                can = (edge[i].weight > 0.35);
            }
            else can = check(tot1, tot2, edge[i].weight);
            if (can)
            {
                father[fay] = fax;
                totp[fax] += totp[fay];
                graph.addedge(edge[i].x, edge[i].y, edge[i].weight);
            }
        }
        else
        {
            graph.addedge(edge[i].x, edge[i].y, edge[i].weight);
            mp[edge[i].x][edge[i].y] = mp[edge[i].y][edge[i].x] = edge[i].weight;
        }
    }
    for (int i = 0; i < totSentence; ++i)
    {
        for (int j = i - 1; j >= 0; --j)
        {
            if (sen[i].ti - sen[j].ti > 45) break;
            if (mp[i][j] > 0.3) printf("%d %d %f\n", i, j, mp[i][j]);
        }
    }
    printf("%d\n\n", graph.totedge);
    memset(v, false, sizeof(v));
    for (int i = 0; i < totSentence; ++i)
    {
        if (!v[i])
        {
            dfs(i);
            printf("\n");
        }
    }
    return 0;
}
