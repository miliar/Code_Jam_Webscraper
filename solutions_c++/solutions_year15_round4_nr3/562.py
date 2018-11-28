#include <cstdio>
#include <set>
#include <string>
//#include <algorithm>
#include <vector>

using namespace std;
//--common
#define forr(i,f,t) for (int i = (f); i <= (t); i++)
#define fori(i,t) for (int i = 0; i < (t); i++)
#define forc(i,c) for (int i = 0; i < (c).size(); i++)
#define forit(it,c) for (auto it = (c).begin(), end = (c).end(); it != end; ++it)

template <typename C> void rerase(C& s, const typename C::const_reverse_iterator &it ) { s.erase(s.find(*it)); }
template <typename T> vector<T>& operator<<(vector<T>& v, const T& t) { v.push_back(t); return v; }
template <typename T> set<T>& operator<<(set<T>& v, const T& t) { v.insert(t); return v; }
//--end common
#include <QString>
#include <QStringList>
#include <QList>
#include <QVector>
#include <QHash>
#include <QSet>


int main(int argc, char *argv[])
{
     int T;
     scanf("%i", &T);
     char * line = (char*)malloc(20000);
     forr (tt, 1, T) {
          int n;
          //char line[20000];
          scanf("%i\n", &n);
          int wordid = 1;
          QHash<QString, int> wordmap;
          QList<QSet<int> > sentences;
          fori (i, n) {
               char * x = line; size_t temp = 20000;
               //fprintf(stderr, "a"); fflush(stdout);
               getline(&x, &temp, stdin);
               //fprintf(stderr, "b"); fflush(stdout);
               QString temps(line);
               QStringList words = temps.trimmed().split(" ");
               //printf("%s\n", qPrintable(words.join(" ")));
               sentences << QSet<int>();
               foreach (const QString& word, words) {
                    if (word.contains(" ")) printf("fail\n");
                    if (!wordmap.contains(word)) wordmap.insert(word, wordid++);
                    sentences.last().insert(wordmap[word]);
               }
          }

          QVector<int> wordoccs; wordoccs.resize(wordid);
          for (int i=0;i<wordid;i++) {
               int occs = 0;
               fori(j, sentences.size())
                         if (sentences[j].contains(i)) occs |= 1 << j;
               wordoccs[ i]=occs;
               //printf(":::%i -> %i\n",i,wordoccs[i]);
          }
          int maxcombinations = 1 << (n - 2);
          int res = wordid + 1;
          for (int C = 0; C < maxcombinations; C++) {
               int D = 1 | (C << 2 );
               int mix = 0;
               for (int i=0;i<wordoccs.size();i++)
                    if ((wordoccs[i] & D) != wordoccs[i]
                         && (wordoccs[i] & D) != 0) mix++;
               if (mix < res) res = mix;
          }
/*
          int maxcombinations = 1 << (n - 2);
          int res = wordid + 1;
          for (int C = 0; C < maxcombinations; C++) {
               QSet<int> english, french;
               fori (i, sentences[0].size())
                         english.insert(sentences[0][i]);
               fori (i, sentences[1].size())
                         french.insert(sentences[1][i]);
               //foreach (int w, sentences[0]) english.insert(w);
               //foreach (int w, sentences[1]) french.insert(w);
               int D = C << 2;
               for (int i=2;i<sentences.size();i++) {
                    QSet<int> &lang = D & (1 << i) ? english : french;
                    fori (j, sentences[i].size())
                              lang.insert(sentences[i][j]);
                    //foreach (int w, sentences[i]) lang.insert(w);
               }
               int s = english.intersect(french).size();
               if (s < res) res = s;
          }
*/
          printf("Case #%i: %i\n", tt, res);
          fflush(stdout);
     }
}
