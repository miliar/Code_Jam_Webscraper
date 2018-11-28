#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

ifstream in("me.txt");
ofstream out("ans.txt");

int regWarPoints(vector<bool> &ord)
{
	//for (int i = 0; i < ord.size(); ++i) out << (ord[i]?"K":"N");
	//out << endl;
	int n = ord.size();
	for (int i = 0; i < n; ++i) 
		if (!ord[i]) n = i;
	if (n*2 == ord.size()) return n;
	ord.erase(ord.begin()+n);
	for (int i = n; i < ord.size(); ++i)
		if (ord[i]) { ord.erase(ord.begin()+i); i = (ord.size()+50); }
	return regWarPoints(ord);
}

int deceitWarPoints(vector<bool> &ord)
{
	/*for (int i = 0; i < ord.size(); ++i) out << (ord[i]?"K":"N");
	out << endl;*/
	int points = 0;
	if (ord.size() > 0 && !ord[ord.size()-1])
	{
		ord.resize(ord.size()-1);
		for (int i = ord.size()-1; i >= 0; --i)
			if (ord[i]) { ord.erase(ord.begin()+i); i = -1; }
		return 1+deceitWarPoints(ord);
	}
	int n = ord.size();
	for (int i = 0; i < n; ++i) 
		if (!ord[i]) n = i;
	if (n*2 == ord.size()) return n;
	ord.erase(ord.begin()+n);
	for (int i = ord.size()-1; i >= 0; --i)
		if (ord[i]) { ord.erase(ord.begin()+i); i = 0; }
	return deceitWarPoints(ord);
}

int main()
{
	int times; in >> times;
	for (int currentTime = 1; currentTime <= times; ++currentTime)
	{
		int numBlocks; in >> numBlocks; int kLen = numBlocks, nLen = numBlocks;
		vector<double> naomi, ken;
		naomi.resize(numBlocks); ken.resize(numBlocks);
		for (int i = 0; i < numBlocks; ++i) in >> naomi[i];
		for (int i = 0; i < numBlocks; ++i) in >> ken[i];
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		vector<bool> blocks; blocks.resize(2*numBlocks);
		vector<double> mBlk; mBlk.resize(2*numBlocks);
		// for (int i = 0; i < nLen; ++i) out << naomi[i] << " "; out << endl;
		// for (int i = 0; i < kLen; ++i) out << ken[i] << " "; out << endl;
		// 0 if naomi, leftmost is smallest
		// 01 could mean naomi has block 0.1kg, ken 0.2kg
		while (kLen > 0 || nLen > 0)
			if (kLen == 0 || (nLen > 0 && naomi[nLen-1] > ken[kLen-1]))
				{ blocks[kLen+nLen-1] = false; mBlk[kLen+nLen-1] = naomi[nLen-1]; --nLen; }
			else{ blocks[kLen+nLen-1] = true;  mBlk[kLen+nLen-1] = ken[kLen-1];   --kLen; }
		/*for (int i = 0; i < 2*numBlocks; ++i) out << mBlk[i] << " ";
		out << endl;
		for (int i = 0; i < 2*numBlocks; ++i) out << (blocks[i]?"K":"N");
		out << endl;*/
		auto blocks2 = blocks;
		out << "Case #" << currentTime << ": " << deceitWarPoints(blocks) << " " << regWarPoints(blocks2) << endl;
		// NOW we have a vector of binary #s containing Naomi's blocks & Ken's blocks in order of weight
	}
}