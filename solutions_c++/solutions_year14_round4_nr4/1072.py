#include <cstdio>
#include <cstring>
#include <cstdlib>#include<iostream>#include<string>#include<set>
char strings[10][15];int servers[5][10];int server_size[5];int max_nodes, max_ways;int num_strings;int num_servers;using namespace std;int count_server_nodes(int server) {	set<string> tree;	char tmp[100];		for (int i = 0; i < server_size[server]; ++i) {		char * dest = strings[servers[server][i]];//		puts(dest);		for (int j = 0; j <= strlen(dest); ++j) {			strncpy(tmp, dest, j);			tmp[j] = 0;			tree.insert(tmp);			//puts(tmp);		}	}	//	for (set<string>::iterator it=tree.begin(); it!=tree.end(); ++it)//		cout << ' ' << *it;//	printf("Size: %d\n", tree.size());		return tree.size();}int count_nodes() {	int sum = 0;	for (int i = 0; i < num_servers; ++i)		sum += count_server_nodes(i);	return sum;}void DFS(int current) {	int i;		if (current >= num_strings) {		for (int i = 0; i < num_servers; ++i)			if (server_size[i] == 0)				return;		int nodes = count_nodes();		if (nodes == max_nodes) {			max_ways++;		}		else if (nodes > max_nodes) {			max_nodes = nodes;			max_ways = 1;		}		return;	}		for (int i = 0; i < num_servers; ++i) {		servers[i][server_size[i]] = current;		server_size[i]++;		DFS(current + 1);		server_size[i]--;	}}
void run() {	max_nodes = 0;	max_ways = 0;	scanf("%d%d", &num_strings, &num_servers);	for (int i = 0; i < num_strings; ++i)		scanf("%s", &strings[i]);	for (int i = 0; i < num_servers; ++i)		server_size[i] = 0;	DFS(0);	printf("%d %d\n", max_nodes, max_ways);}

int main() {
    int num_cases;
    scanf("%d", &num_cases);
    for (int t = 1; t <= num_cases; ++t) {
        printf("Case #%d: ", t);
        run();
    }
    return 0;
}

