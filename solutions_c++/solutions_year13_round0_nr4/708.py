#include <iostream>
#include <cstdio>
#include <cstring>

int keys[500];
int qt_keys;

int keys_inside[201][500];
int keys_inside_ct[201];

int k, n;

bool opened[201];
int opened_by[201];
int qt_opened;

int res[201];
int res_ct;

int queue[300];
int queue_begin, queue_end;
int queue_var;
bool state[1<<22];
int curr_state;

#define enqueue(x) do{ queue[queue_end++] = x; queue_end = queue_end == 300 ? 0 : queue_end; } while(0)
#define dequeue() (queue_var = queue[queue_begin++]; queue_begin = queue_begin == 300 ? 0 : queue_begin; queue_var)

bool go()
{
  bool has_not_opened = false;

  if(state[curr_state]) return false;
  state[curr_state] = true;

  for(int i = 0; i < n; i++)
  {
    if(!opened[i])
    {
      has_not_opened = true;
      if(keys[opened_by[i]])
      {
        keys[opened_by[i]]--;
        opened[i] = true;

        for(int j = 0; j < keys_inside_ct[i]; j++)
        {
          keys[keys_inside[i][j]]++;
        }

        res[res_ct++] = i;

        curr_state |= (1<<i);
        
        if(go()) return true;

        curr_state ^= (1<<i);

        res_ct--;
 
        for(int j = 0; j < keys_inside_ct[i]; j++)
        {
          keys[keys_inside[i][j]]--;
        }

        keys[opened_by[i]]++;
        opened[i] = false;
      }
    }
  }

  return !has_not_opened;
}

int main(void)
{
  int cases;

  scanf("%d\n", &cases);

  for(int cas = 1; cas <= cases; cas++)
  {
    scanf("%d %d\n", &k, &n);

    memset(keys_inside_ct, 0, sizeof(keys_inside_ct));
    memset(opened, 0, sizeof(opened));
    memset(keys, 0, sizeof(keys));
    memset(state, 0, sizeof(state));

    qt_keys = k;
    qt_opened = 0;
    queue_begin = queue_end = 0;
    curr_state = 0;

    res_ct = 0;

    for(int i = 0; i < k; i++)
    {
      int key;
      scanf("%d", &key);
      keys[key]++;
    }

    for(int i = 0; i < n; i++)
    {
      int type;
      scanf("%d %d", &type, &keys_inside_ct[i]);

      opened_by[i] = type;

      for(int j = 0; j < keys_inside_ct[i]; j++)
      {
        scanf("%d", &keys_inside[i][j]);
      }
    }

    printf("Case #%d: ", cas);
    if(go())
    {
      printf("%d", res[0]+1);
      for(int i = 1; i < n; i++) printf(" %d", res[i]+1);
      printf("\n");
    }
    else
    {
      printf("IMPOSSIBLE\n");
    }
  }

  return 0;
}
