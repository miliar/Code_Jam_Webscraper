#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <map>


using namespace std;

struct info
{
	char a;
	bool neg;
	info(char x, bool y):a(x), neg(y){}
	info():a('t'), neg(false){}
};

map<pair<char, char>, info> mapMulti;
map<pair<char, char>, info> mapDivi;
map<pair<char, char>, info> mapDivi2;

void initmap()
{
	mapMulti[make_pair('1', '1')] = info('1', false);
	mapMulti[make_pair('1', 'i')] = info('i', false);
	mapMulti[make_pair('1', 'j')] = info('j', false);
	mapMulti[make_pair('1', 'k')] = info('k', false);
	mapMulti[make_pair('i', '1')] = info('i', false);
	mapMulti[make_pair('i', 'i')] = info('1', true);
	mapMulti[make_pair('i', 'j')] = info('k', false);
	mapMulti[make_pair('i', 'k')] = info('j', true);
	mapMulti[make_pair('j', '1')] = info('j', false);
	mapMulti[make_pair('j', 'i')] = info('k', true);
	mapMulti[make_pair('j', 'j')] = info('1', true);
	mapMulti[make_pair('j', 'k')] = info('i', false);
	mapMulti[make_pair('k', '1')] = info('k', false);
	mapMulti[make_pair('k', 'i')] = info('j', false);
	mapMulti[make_pair('k', 'j')] = info('i', true);
	mapMulti[make_pair('k', 'k')] = info('1', true);

	mapDivi[make_pair('1', '1')] = info('1', false);
	mapDivi[make_pair('1', 'i')] = info('i', true);
	mapDivi[make_pair('1', 'j')] = info('j', true);
	mapDivi[make_pair('1', 'k')] = info('k', true);

	mapDivi[make_pair('i', '1')] = info('i', false);
	mapDivi[make_pair('i', 'i')] = info('1', false);
	mapDivi[make_pair('i', 'j')] = info('k', false);
	mapDivi[make_pair('i', 'k')] = info('j', true);

	mapDivi[make_pair('j', '1')] = info('j', false);
	mapDivi[make_pair('j', 'i')] = info('k', true);
	mapDivi[make_pair('j', 'j')] = info('1', false);
	mapDivi[make_pair('j', 'k')] = info('i', false);

	mapDivi[make_pair('k', '1')] = info('k', false);
	mapDivi[make_pair('k', 'i')] = info('j', false);
	mapDivi[make_pair('k', 'j')] = info('i', true);
	mapDivi[make_pair('k', 'k')] = info('1', false);

	mapDivi2[make_pair('1', '1')] = info('1', false);
	mapDivi2[make_pair('1', 'i')] = info('i', true);
	mapDivi2[make_pair('1', 'j')] = info('j', true);
	mapDivi2[make_pair('1', 'k')] = info('k', true);

	mapDivi2[make_pair('i', '1')] = info('i', false);
	mapDivi2[make_pair('i', 'i')] = info('1', false);
	mapDivi2[make_pair('i', 'j')] = info('k', true);
	mapDivi2[make_pair('i', 'k')] = info('j', false);

	mapDivi2[make_pair('j', '1')] = info('j', false);
	mapDivi2[make_pair('j', 'i')] = info('k', false);
	mapDivi2[make_pair('j', 'j')] = info('1', false);
	mapDivi2[make_pair('j', 'k')] = info('i', true);

	mapDivi2[make_pair('k', '1')] = info('k', false);
	mapDivi2[make_pair('k', 'i')] = info('j', true);
	mapDivi2[make_pair('k', 'j')] = info('i', false);
	mapDivi2[make_pair('k', 'k')] = info('1', false);
}

info multi(const info& a, const info& b)
{
	info c = mapMulti[make_pair(a.a, b.a)];
	bool neg = a.neg^b.neg ^ c.neg;
	c.neg = neg;
	return c;
}

info devide(const info&a, const info& b)
{
	info  c = mapDivi[make_pair(a.a, b.a)];
	bool neg = a.neg ^ b.neg ^ c.neg;
	c.neg = neg;
	return c;
}

info devide2(const info&a, const info& b)
{
	info  c = mapDivi2[make_pair(a.a, b.a)];
	bool neg = a.neg ^ b.neg ^ c.neg;
	c.neg = neg;
	return c;
}
int main(int argc, char **argv)
{
	initmap();
	ifstream in(argv[1]);
	int nCase;
	in >> nCase;
	for (int i = 1; i <= nCase; i++){
		int nNum ;
		in >> nNum;
		int repeat;
		in >> repeat;
		string str;
		in >>str;
		string strfinal;
		while (repeat -- > 0){
			strfinal += str;
		}
		str = strfinal;
		info final = info('1', false);
		vector<int> head;
		vector<int> tail;
		for (int j = 0; j < str.size(); j++){
			final = multi(final, info(str[j], false));
			if (final.a == 'i' && !final.neg){
				head.push_back(j);
			}
		}
		info final2 = info('1', false);
		for (int j = str.size()-1; j >= 0; j--)
		{
			final2 = multi(info(str[j], false), final2);
			if (final2.a == 'k' && !final2.neg){
				tail.push_back(j);
			}
		}
		bool find = false;
		for (int ii = 0; ii < head.size() && !find; ii++){
			for (int jj = 0; jj < tail.size(); jj++){
				if (tail[jj] <= head[ii]){
					break;
				}
				info tail = devide(final, info('i', false));
				info mid = devide2(tail, info('k', false));
				if (mid.a == 'j' && !mid.neg){
					find = true;
					break;
				}
			}
		}
		if (find){
			cout<<"Case #"<<i<<": YES"<<endl;
		}
		else {
			cout<<"Case #"<<i<<": NO"<<endl;
		}
	}
	return 0;
}
