#include <iostream>
#include <cstdint>
#include <map>
#include <vector>
#include <algorithm>

struct Event
{
    enum class Dir { IN, OUT } dir;
    uint64_t stop;
    uint64_t amount;

    bool operator<(Event const& i2) const
    {
        if(stop < i2.stop) return true;
        if(stop > i2.stop) return false;

        return dir < i2.dir;
    }
};

uint64_t solve()
{
    uint64_t stopCount, pairCount;
    uint64_t regular = 0;

    std::cin >> stopCount >> pairCount;

    std::vector<Event> events;
    events.resize(pairCount * 2);
    for(uint64_t i = 0; i < pairCount; i++)
    {
        uint64_t from, to, amount;

        std::cin >> from >> to >> amount;

        events[i * 2].dir = Event::Dir::IN;
        events[i * 2].stop = from;
        events[i * 2].amount = amount;

        events[i * 2 + 1].dir = Event::Dir::OUT;
        events[i * 2 + 1].stop = to;
        events[i * 2 + 1].amount = amount;

        uint64_t dist = to - from;
        regular += (dist * dist - dist) / 2 * amount;
    }
    std::sort(events.begin(), events.end());

    std::map<uint64_t, uint64_t> people;

    uint64_t lastStop = 1;
    uint64_t save = 0;
    for(Event const& event : events)
    {
        uint64_t b = lastStop;
        uint64_t e = event.stop;

        for(std::pair<uint64_t, uint64_t> const& person : people)
        {
            uint64_t from = person.first;

            save += ((e * e) - (2 * from + 1) * e - (b * b) + (2 * from + 1) * b) / 2 * person.second;
        }

        if(event.dir == Event::Dir::IN)
        {
            people[event.stop] += event.amount;
        }
        else if(event.dir == Event::Dir::OUT)
        {
            uint64_t left = event.amount;

            for(auto it = people.rbegin(); it != people.rend();)
            {
                uint64_t a = std::min(left, it->second);
                it->second -= a;
                left -= a;

                /*if(it->second == 0)
                {
                    people.erase(it++);
                }
                else*/
                {
                    ++it;
                }

                if(left == 0)
                {
                    break;
                }
            }
        }

        lastStop = event.stop;
    }

    return (save - regular) % 1000002013;
}

int main()
{
    uint64_t cases;

    std::cin >> cases;
    for(uint64_t i = 1; i <= cases; i++)
    {
        std::cout << "Case #" << i << ": " << solve() << std::endl;
    }
}
